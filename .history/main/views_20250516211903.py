from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.models import User  # Custom User model

# Trang chính sau khi login
from django.contrib.auth.decorators import login_required
from nutrition.forms import GoalSelectionForm
from nutrition.models import GoalRecommendation
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

@login_required
def generate_meal_plan(request):
    user = request.user
    bmi = user.bmi
    recommendation = None
    saved_plan = None

    if request.method == 'POST':
        form = GoalSelectionForm(request.POST)
        if form.is_valid():
            goal = form.cleaned_data['goal_type']
            calorie = form.cleaned_data['calorie_target']
            carbs = form.cleaned_data['carbs']
            protein = form.cleaned_data['protein']
            fat = form.cleaned_data['fat']

            # Lưu lại cho user
            SavedMealPlan.objects.update_or_create(
                user=user,
                defaults={
                    'goal_type': goal,
                    'calorie_target': calorie,
                    'carbs': carbs,
                    'protein': protein,
                    'fat': fat,
                }
            )

            recommendation = {
                'calories': calorie,
                'carbs': carbs,
                'protein': protein,
                'fat': fat,
            }

    else:
        try:
            saved_plan = SavedMealPlan.objects.get(user=user)
            form = GoalSelectionForm(initial={
                'goal_type': saved_plan.goal_type,
                'calorie_target': saved_plan.calorie_target,
                'carbs': saved_plan.carbs,
                'protein': saved_plan.protein,
                'fat': saved_plan.fat,
            })
            recommendation = {
                'calories': saved_plan.calorie_target,
                'carbs': saved_plan.carbs,
                'protein': saved_plan.protein,
                'fat': saved_plan.fat,
            }
        except SavedMealPlan.DoesNotExist:
            form = GoalSelectionForm()

    return render(request, 'main/generate_meal_plan.html', {
        'form': form,
        'recommendation': recommendation
    })


    
def generate_exercises(request):
    return render(request, 'main/generate_exercises.html')

def nutrition(request):
    return render(request, 'main/nutrition.html')

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

