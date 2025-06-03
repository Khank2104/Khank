from django.urls import path
from . import views

urlpatterns = [
    path('generate_meal_plan/', views.generate_meal_plan, name='generate_meal_plan'),
]
