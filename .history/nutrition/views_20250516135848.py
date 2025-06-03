from django.shortcuts import render
from .forms import GoalSelectionForm
from .models import GoalRecommendation

def generate_meal_plan(request):
    form = GoalSelectionForm(request.POST or None)
    calories = carbs = protein = fat = 0

    if request.method == 'POST' and form.is_valid():
        goal_type = form.cleaned_data['goal_type']
        bmi = request.user.bmi  # cần đảm bảo user có BMI

        # Tìm bản ghi phù hợp với BMI và mục tiêu
        recommendation = GoalRecommendation.objects.filter(
            goal_type=goal_type,
            bmi_min__lte=bmi,
            bmi_max__gte=bmi
        ).first()

        if recommendation:
            form.fields['calorie_target'].initial = recommendation.calories
            form.fields['carbs'].initial = recommendation.carbs
            form.fields['protein'].initial = recommendation.protein
            form.fields['fat'].initial = recommendation.fat

    return render(request, 'main/generate_meal_plan.html', {'form': form})
