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

def authenticate(request):
    return render(request, 'main/authenticate.html')