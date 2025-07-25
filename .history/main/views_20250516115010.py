from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.models import User  # Custom User model

# Trang chính sau khi login
from django.contrib.auth.decorators import login_required

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

def generate_meal_plan(request):
    return render(request, 'main/generate_meal_plan.html')

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

