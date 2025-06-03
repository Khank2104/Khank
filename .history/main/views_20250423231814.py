from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'main/dashboard.html')

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

def profile(request):
    return render(request, 'main/profile.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import User  # your custom user

def authenticate_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Use custom email-based authentication
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Email hoặc mật khẩu không đúng.')

    return render(request, 'main/authenticate.html')
