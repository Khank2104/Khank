from django.urls import path
from .views import generate_meal_plan

urlpatterns = [
    path('generate_meal_plan/', generate_meal_plan, name='generate_meal_plan'),
]
