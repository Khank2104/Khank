from django import forms
from .models import FoodEntry

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


class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ['meal_type', 'food_name', 'calories', 'carbs', 'protein', 'fat', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'meal_type': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'food_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'calories': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'}),
            'carbs': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'}),
            'protein': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'}),
            'fat': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'}),