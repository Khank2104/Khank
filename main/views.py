from django.shortcuts import render
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.models import User  # Custom User model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from nutrition.forms import GoalSelectionForm
from nutrition.models import GoalRecommendation, SavedMealPlan
# Trang chính sau khi login
from django.contrib.auth.decorators import login_required
from nutrition.forms import GoalSelectionForm
from nutrition.models import GoalRecommendation
from nutrition.forms import FoodEntryForm
from nutrition.models import FoodEntry
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date
from nutrition.models import SavedMealPlan, SuggestedMeal, FoodEntry
from nutrition.forms import FoodEntryForm
from hydration.models import WaterIntake
from sleep.models import SleepRecord
LOGIN_URL = '/authenticate/'

@login_required
def dashboard(request):
    user = request.user
    today = timezone.now().date()  # Lấy ngày hôm nay theo Django timezone
    # Tổng lượng nước uống hôm nay từ bảng WaterIntake
    total_water_today = WaterIntake.objects.filter(user=user, date=today).aggregate(Sum('amount_ml'))['amount_ml__sum'] or 0
    # Tổng thời gian ngủ hôm nay từ bảng SleepRecord
    today_sleep_record = SleepRecord.objects.filter(user=user, date=today).first()
    total_sleep_today = today_sleep_record.duration_hours if today_sleep_record else 0  # Lấy giá trị thực nếu có, nếu không hiển thị mặc định 7h
    

    return render(request, 'main/dashboard.html', {
        'name': user.get_full_name(),
        'bmi': user.bmi,
        'weight': user.weight_kg,
        'height': user.height_cm,
        'email': user.email,
        'water': total_water_today,   # bạn có thể lấy từ WaterIntake sau
        'sleep': total_sleep_today, 
        'last_update': user.last_weight_update  
    })



# Landing page 
def index(request):
    return render(request, 'main/index.html')

from django.http import JsonResponse
from django.db.models import Sum
from django.db.models.functions import Coalesce
from fitness.models import Activity, SavedExercisePlan, ExerciseSuggestion

@login_required
def activity(request):
    user = request.user
    today = date.today()

    if request.method == 'POST':
        Activity.objects.create(
            user=user,
            activity_type=request.POST.get('activity_type'),
            duration_minutes=int(request.POST.get('duration')),
            calories_burned=int(request.POST.get('calories')),
            date=request.POST.get('date', today)  # Mặc định lấy hôm nay nếu không nhập ngày
        )
        return redirect('activity')

    # Lấy các hoạt động trong ngày
    activities_today = Activity.objects.filter(user=user, date=today)

    # Tổng hợp thống kê
    summary = activities_today.aggregate(
        total_minutes=Sum('duration_minutes'),
        total_calories=Sum('calories_burned')
    )

    # Lấy gợi ý bài tập từ kế hoạch đã lưu
    suggested_exercises = []
    try:
        plan = SavedExercisePlan.objects.get(user=user)
        suggested_exercises = ExerciseSuggestion.objects.filter(
            goal=plan.goal,
            level=plan.level,
            duration__lte=plan.duration,
            bmi_min__lte=user.bmi,
            bmi_max__gte=user.bmi
        )[:4]
    except SavedExercisePlan.DoesNotExist:
        pass

    return render(request, 'main/activity.html', {
        'activities_today': activities_today,
        'summary': summary,
        'suggested_exercises': suggested_exercises,
    })

# API trả về dữ liệu để cập nhật biểu đồ
@login_required
def activity_data(request):
    today = date.today()
    summary = Activity.objects.filter(user=request.user, date=today).aggregate(
        total_minutes=Coalesce(Sum('duration_minutes'), 0),
        total_calories=Coalesce(Sum('calories_burned'), 0)
    )
    return JsonResponse(summary)

from django.shortcuts import get_object_or_404
from fitness.models import Activity
from datetime import date

@login_required
def edit_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id, user=request.user)

    if request.method == 'POST':
        activity.activity_type = request.POST.get('activity_type')
        activity.duration_minutes = request.POST.get('duration')
        activity.calories_burned = request.POST.get('calories')
        activity.date = request.POST.get('date')
        activity.save()
        return redirect('activity')

    return render(request, 'main/edit_activity.html', {'activity': activity})


@login_required
def delete_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id, user=request.user)

    if request.method == 'POST':
        activity.delete()
        return redirect('activity')

    return render(request, 'main/deleted_confirm.html', {'activity': activity})



from nutrition.models import GoalRecommendation, SavedMealPlan

from nutrition.models import GoalRecommendation, SavedMealPlan, SuggestedMeal

@login_required
def generate_meal_plan(request):
    user = request.user
    bmi = user.bmi
    recommendation = None
    suggested_meals = []
    form = GoalSelectionForm()

    if request.method == 'POST':
        form = GoalSelectionForm(request.POST)
        if form.is_valid():
            goal = form.cleaned_data['goal_type']

            # Lấy đề xuất dinh dưỡng từ bảng GoalRecommendation
            rec = GoalRecommendation.objects.filter(
                goal_type=goal,
                bmi_min__lte=bmi,
                bmi_max__gte=bmi
            ).first()

            if rec:
                # Update lại form với dữ liệu mới
                form = GoalSelectionForm(initial={
                    'goal_type': goal,
                    'calorie_target': rec.calories,
                    'carbs': rec.carbs,
                    'protein': rec.protein,
                    'fat': rec.fat,
                })

                recommendation = {
                    'calories': rec.calories,
                    'carbs': rec.carbs,
                    'protein': rec.protein,
                    'fat': rec.fat,
                }

                # Gợi ý món ăn
                suggested_meals = SuggestedMeal.objects.filter(
                    goal_type=goal,
                    bmi_min__lte=bmi,
                    bmi_max__gte=bmi
                )

    else:
        try:
            saved = SavedMealPlan.objects.get(user=user)
            form = GoalSelectionForm(initial={
                'goal_type': saved.goal_type,
                'calorie_target': saved.calorie_target,
                'carbs': saved.carbs,
                'protein': saved.protein,
                'fat': saved.fat,
            })
            recommendation = {
                'calories': saved.calorie_target,
                'carbs': saved.carbs,
                'protein': saved.protein,
                'fat': saved.fat,
            }
            suggested_meals = SuggestedMeal.objects.filter(
                goal_type=saved.goal_type,
                bmi_min__lte=bmi,
                bmi_max__gte=bmi
            )
        except SavedMealPlan.DoesNotExist:
            form = GoalSelectionForm()

    return render(request, 'main/generate_meal_plan.html', {
        'form': form,
        'recommendation': recommendation,
        'suggested_meals': suggested_meals,
    })

@login_required
def save_meal_plan(request):
    if request.method == 'POST':
        form = GoalSelectionForm(request.POST)
        if form.is_valid():
            SavedMealPlan.objects.update_or_create(
                user=request.user,
                defaults={
                    'goal_type': form.cleaned_data['goal_type'],
                    'calorie_target': form.cleaned_data['calorie_target'],
                    'carbs': form.cleaned_data['carbs'],
                    'protein': form.cleaned_data['protein'],
                    'fat': form.cleaned_data['fat'],
                }
            )
    return redirect('generate_meal_plan')


    
    
from fitness.models import ExerciseSuggestion

from fitness.forms import ExerciseFilterForm

from fitness.models import SavedExercisePlan

@login_required
def generate_exercises(request):
    suggested_exercises = []
    initial_data = {}
    
    try:
        saved = SavedExercisePlan.objects.get(user=request.user)
        initial_data = {
            'goal': saved.goal,
            'level': saved.level,
            'duration': saved.duration
        }
    except SavedExercisePlan.DoesNotExist:
        pass

    form = ExerciseFilterForm(initial=initial_data)

    if request.method == 'POST':
        form = ExerciseFilterForm(request.POST)
        if form.is_valid():
            goal = form.cleaned_data['goal']
            level = form.cleaned_data['level']
            duration = form.cleaned_data['duration']
            bmi = request.user.bmi

            suggested_exercises = ExerciseSuggestion.objects.filter(
                goal=goal,
                level=level,
                duration__lte=duration,
                bmi_min__lte=bmi,
                bmi_max__gte=bmi
            )[:4]

    return render(request, 'main/generate_exercises.html', {
        'form': form,
        'suggested_exercises': suggested_exercises
    })


from fitness.models import SavedExercisePlan

from fitness.models import SavedExercisePlan

from django.urls import reverse
from django.http import HttpResponseRedirect

from django.urls import reverse
from django.http import HttpResponseRedirect

@login_required
def save_exercise_plan(request):
    if request.method == 'POST':
        goal = request.POST.get('goal')
        level = request.POST.get('level')
        duration = request.POST.get('duration')

        if goal and level and duration:
            SavedExercisePlan.objects.update_or_create(
                user=request.user,
                defaults={
                    'goal': goal,
                    'level': level,
                    'duration': duration
                }
            )
    # 👉 Redirect lại không cần query string
    return redirect('generate_exercises')




@login_required
def nutrition(request):
    user = request.user
    today = date.today()

    saved_plan = None
    suggested_meals = []
    entries = FoodEntry.objects.filter(user=user, date=today)
    # Tính tổng dinh dưỡng trong ngày
    totals = entries.aggregate(
        total_carbs=Sum('carbs'),
        total_protein=Sum('protein'),
        total_fat=Sum('fat'),
    )

    if request.method == 'POST':
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.user = user
            new_entry.save()
            return redirect('nutrition')
    else:
        form = FoodEntryForm()

    try:
        saved_plan = SavedMealPlan.objects.get(user=user)
        bmi = user.bmi
        suggested_meals = SuggestedMeal.objects.filter(
            goal_type=saved_plan.goal_type,
            bmi_min__lte=bmi,
            bmi_max__gte=bmi
        )
    except SavedMealPlan.DoesNotExist:
        pass

    return render(request, 'main/nutrition.html', {
        'saved_plan': saved_plan,
        'suggested_meals': suggested_meals,
        'entries': entries,
        'form': form,
        'totals': totals,  # <== truyền vào template
    })


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from sleep.models import SleepRecord
from sleep.forms import SleepRecordForm
from datetime import date
from django.db.models import Avg

from datetime import datetime, timedelta
from django.db.models import Avg
from sleep.models import SleepRecord
from sleep.forms import SleepRecordForm

from datetime import datetime, timedelta
from django.db.models import Avg
from sleep.models import SleepRecord
from sleep.forms import SleepRecordForm

@login_required
def sleep(request):
    user = request.user
    today = date.today()
    today_record = SleepRecord.objects.filter(user=user, date=today).first()

    form = SleepRecordForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        record = form.save(commit=False)
        record.user = user

        try:
            # Chuyển time thành datetime để tính duration
            sleep_dt = datetime.combine(record.date, record.sleep_time)
            wake_dt = datetime.combine(record.date, record.wake_time)

            if wake_dt <= sleep_dt:
                wake_dt += timedelta(days=1)

            record.duration_hours = round((wake_dt - sleep_dt).total_seconds() / 3600, 2)
            record.save()
            return redirect('sleep')
        except Exception as e:
            print("Lỗi tính thời gian:", e)

    elif request.method == 'POST':
        print("❗ Form lỗi:", form.errors)

    # Get dữ liệu tuần
    week_data = SleepRecord.objects.filter(user=user).order_by('-date')[:7]
    avg_duration = week_data.aggregate(avg=Avg('duration_hours'))['avg'] or 0

    return render(request, 'main/sleep.html', {
        'form': form,
        'today_record': today_record,
        'sleep_logs': week_data,
        'avg_duration': round(avg_duration, 1)
    })



@login_required
def edit_sleep(request, pk):
    record = get_object_or_404(SleepRecord, id=pk, user=request.user)
    form = SleepRecordForm(request.POST or None, instance=record)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('sleep')
    return render(request, 'main/edit_sleep.html', {'form': form, 'entry': record})

@login_required
def delete_sleep(request, pk):
    record = get_object_or_404(SleepRecord, id=pk, user=request.user)
    if request.method == 'POST':
        record.delete()
        return redirect('sleep')
    return render(request, 'main/delete_sleep.html', {'entry': record})




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from hydration.models import WaterIntake
from hydration.forms import WaterIntakeForm
from datetime import date
from django.db.models import Sum
from django.http import JsonResponse
from django.db.models.functions import Coalesce

@login_required
def water_intake(request):
    user = request.user
    today = date.today()

    if request.method == 'POST':
        form = WaterIntakeForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = user
            entry.save()
            return redirect('water_intake')
    else:
        form = WaterIntakeForm()

    # Tổng lượng nước hôm nay
    today_entries = WaterIntake.objects.filter(user=user, date=today)
    total_today = today_entries.aggregate(total=Sum('amount_ml'))['total'] or 0

    # Log tất cả
    all_entries = WaterIntake.objects.filter(user=user).order_by('-date', '-time')

    return render(request, 'main/water_intake.html', {
        'form': form,
        'entries': all_entries,
        'total_today': total_today,
        'goal_ml': 2000,
    })
# API trả về tổng lượng nước uống trong ngày để cập nhật biểu đồ
@login_required
def water_intake_data(request):
    today = date.today()
    summary = WaterIntake.objects.filter(user=request.user, date=today).aggregate(
        total=Coalesce(Sum('amount_ml'), 0)
    )
    return JsonResponse(summary)


@login_required
def edit_water_intake(request, pk):
    entry = get_object_or_404(WaterIntake, id=pk, user=request.user)
    form = WaterIntakeForm(request.POST or None, instance=entry)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('water_intake')
    return render(request, 'main/edit_water.html', {'form': form, 'entry': entry})

@login_required
def delete_water_intake(request, pk):
    entry = get_object_or_404(WaterIntake, id=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('water_intake')
    return render(request, 'main/delete_water.html', {'entry': entry})



from accounts.forms import UserProfileForm  
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'main/profile.html', {
        'form': form,
        'user': user
    })


def about(request):
    return render(request, 'main/about.html')

def service(request):
    return render(request, 'main/service.html')

def contact(request):
    return render(request, 'main/contact.html')


def base(request):
    return render(request, 'main/base.html')

# Trang đăng nhập
def authenticate_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Email hoặc mật khẩu không đúng.")
    else:
        # Kiểm tra nếu người dùng bị redirect tới từ login_required
        if 'next' in request.GET:
            messages.warning(request, "Bạn cần đăng nhập để tiếp tục.")

    return render(request, 'main/authenticate.html')



from accounts.forms import SignupForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'main/authenticate.html', {'signup_form': form})


from django.shortcuts import get_object_or_404

@login_required
def edit_food_entry(request, entry_id):
    entry = get_object_or_404(FoodEntry, id=entry_id, user=request.user)

    if request.method == 'POST':
        form = FoodEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('nutrition')
    else:
        form = FoodEntryForm(instance=entry)

    return render(request, 'main/edit_food_entry.html', {
        'form': form,
        'entry': entry
    })

@login_required
def delete_food_entry(request, entry_id):
    entry = get_object_or_404(FoodEntry, id=entry_id, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('nutrition')
    return render(request, 'main/delete_confirm.html', {'entry': entry})