from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Trang mặc định sau đăng nhập
    path('index/', views.index, name='index'),    # Trang landing (giới thiệu, landing page)
    path('activity/', views.activity, name='activity'),
    path('generate_meal_plan/', views.generate_meal_plan, name='generate_meal_plan'),
    path('generate_exercises/', views.generate_exercises, name='generate_exercises'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('sleep/', views.sleep, name='sleep'),
    path('water_intake/', views.water_intake, name='water_intake'),
    path('profile/', views.profile, name='profile'),
    path('authenticate/', views.authenticate_view, name='authenticate'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
]
