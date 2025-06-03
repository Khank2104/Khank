# nutrition/views.py

from django.shortcuts import render
from .models import GoalRecommendation
from django.contrib.auth.decorators import login_required

@login_required
def user_goal_view(request):
    # Đây chỉ là mock, bạn có thể update logic sau
    return render(request, 'nutrition/user_goal.html', {})
