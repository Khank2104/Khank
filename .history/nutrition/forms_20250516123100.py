from django import forms
from .models import UserGoal

class UserGoalForm(forms.ModelForm):
    class Meta:
        model = UserGoal
        fields = [
            'goal_type',
            'calorie_target',
            'diet_preference',
            'carb_ratio',
            'protein_ratio',
            'fat_ratio'
        ]
