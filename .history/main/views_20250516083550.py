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

def index(request):
    return render(request, 'main/index.html')



def about(request):
    return render(request, 'main/about.html')


def service(request):
    return render(request, 'main/service.html')


def contact(request):
    return render(request, 'main/contact.html')


def base(request):
    return render(request, 'main/base.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import User  # your custom user

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def authenticate_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Email hoặc mật khẩu không đúng.")

    return render(request, 'main/authenticate.html')
