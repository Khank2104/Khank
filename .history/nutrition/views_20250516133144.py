from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserGoalForm
from .models import GoalRecommendation, UserGoal

@login_required
def generate_meal_plan(request):
    user = request.user
    bmi = user.bmi  # Lấy BMI từ profile

    if request.method == 'POST':
        form = UserGoalForm(request.POST)
        if form.is_valid():
            user_goal, created = UserGoal.objects.get_or_create(user=user)
            for field in form.cleaned_data:
                setattr(user_goal, field, form.cleaned_data[field])
            user_goal.save()
            return redirect('nutrition')  # Redirect lại trang nutrition chính

    else:
        # Form mặc định
        form = UserGoalForm()
        recommendation = None

        # Nếu người dùng đã chọn mục tiêu trước đó, lấy lại gợi ý phù hợp BMI
        goal_type = request.GET.get('goal')  # vd: /generate_meal_plan/?goal=weight_loss
        if goal_type and bmi:
            recommendation = GoalRecommendation.objects.filter(
                goal_type=goal_type,
                bmi_min__lte=bmi,
                bmi_max__gte=bmi
            ).first()

            if recommendation:
                form = UserGoalForm(initial={
                    'goal_type': goal_type,
                    'calorie_target': recommendation.calories,
                    'carbs': recommendation.carbs,
                    'protein': recommendation.protein,
                    'fat': recommendation.fat,
                })

    return render(request, 'nutrition/generate_meal_plan.html', {
        'form': form,
        'bmi': bmi,
    })
