from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import GoalRecommendation
from .forms import GoalSelectionForm

@login_required
def generate_meal_plan(request):
    user = request.user
    bmi = user.bmi
    recommendation = None

    if request.method == 'POST':
        form = GoalSelectionForm(request.POST)
        if form.is_valid():
            goal_type = form.cleaned_data['goal_type']
            recommendation = GoalRecommendation.objects.filter(
                goal_type=goal_type,
                bmi_min__lte=bmi,
                bmi_max__gte=bmi
            ).first()
    else:
        form = GoalSelectionForm()

    return render(request, 'main/generate_meal_plan.html', {
        'form': form,
        'recommendation': recommendation
    })
