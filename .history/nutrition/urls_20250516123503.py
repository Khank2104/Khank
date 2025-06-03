from django.urls import path
from . import views

urlpatterns = [
    path('goal/', views.user_goal_view, name='user_goal'),
]
