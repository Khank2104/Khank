from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserGoalForm
from .models import UserGoal

@login_required
def user_goal_view(request):
    try:
        goal = request.user.usergoal
        form = UserGoalForm(instance=goal)
    except UserGoal.DoesNotExist:
        form = UserGoalForm()

    if request.method == 'POST':
        form = UserGoalForm(request.POST, instance=getattr(request.user, 'usergoal', None))
        if form.is_valid():
            user_goal = form.save(commit=False)
            user_goal.user = request.user
            user_goal.save()
            return redirect('dashboard')

    return render(request, 'nutrition/user_goal.html', {'form': form})
