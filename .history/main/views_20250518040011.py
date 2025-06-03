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
LOGIN_URL = '/authenticate/'

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'main/dashboard.html', {
        'name': user.get_full_name(),
        'bmi': user.bmi,
        'weight': user.weight_kg,
        'height': user.height_cm,
        'email': user.email,
        'water': 1500,   # bạn có thể lấy từ WaterIntake sau
        'sleep': 7,      # bạn có thể lấy từ SleepLog sau
    })



# Landing page - như trang giới thiệu công ty
def index(request):
    return render(request, 'main/index.html')

def activity(request):
    return render(request, 'main/activity.html')

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

@login_required
def generate_exercises(request):
    suggested_exercises = []
    form = ExerciseFilterForm()

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


def sleep(request):
    return render(request, 'main/sleep.html')

def water_intake(request):
    return render(request, 'main/water_intake.html')

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



