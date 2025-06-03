from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import GoalRecommendation
from .forms import GoalSelectionForm

@login_required
def generate_meal_plan(request):
    form = GoalSelectionForm(request.POST or None)
    recommendation = None

    bmi = request.user.bmi  # giả sử trường này có sẵn

    if form.is_valid():
        goal_type = form.cleaned_data['goal_type']
        recommendation = GoalRecommendation.objects.filter(
            goal_type=goal_type,
            bmi_min__lte=bmi,
            bmi_max__gte=bmi
        ).first()

    return render(request, 'nutrition/generate_meal_plan.html', {
        'form': form,
        'recommendation': recommendation,
    })
