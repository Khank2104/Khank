from django import forms

GOAL_CHOICES = [
    ('weight_loss', 'Weight Loss'),
    ('muscle_gain', 'Muscle Gain'),
    ('maintenance', 'Maintenance'),
    ('energy', 'Improve Energy'),
]

class GoalSelectionForm(forms.Form):
    goal_type = forms.ChoiceField(choices=GOAL_CHOICES, label='Health Goal')

    # Các trường còn lại để readonly (không required)
    calorie_target = forms.IntegerField(label='Daily Calorie Target (kcal)', required=False)
    carbs = forms.IntegerField(label='Carbohydrates (g)', required=False)
    protein = forms.IntegerField(label='Protein (g)', required=False)
    fat = forms.IntegerField(label='Fat (g)', required=False)
