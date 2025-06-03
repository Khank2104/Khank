# nutrition/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Ví dụ placeholder, bạn có thể thêm các URL thực sau
    path('goal/', views.user_goal_view, name='user_goal'),  # nếu bạn dùng view này
    # hoặc để tạm:
    # path('', views.nutrition_home, name='nutrition_home'),
]
