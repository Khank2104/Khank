from django import forms

GOAL_CHOICES = [
    ('weight_loss', 'Weight Loss'),
    ('muscle_gain', 'Muscle Gain'),
    ('maintenance', 'Maintenance'),
    ('energy', 'Improve Energy'),
]

class GoalSelectionForm(forms.Form):
    goal_type = forms.ChoiceField(choices=GOAL_CHOICES, label='Health Goal')
    calorie_target = forms.IntegerField(label='Daily Calorie Target (kcal)')
    carbs = forms.IntegerField(label='Carbohydrates (g)')
    protein = forms.IntegerField(label='Protein (g)')
    fat = forms.IntegerField(label='Fat (g)')
