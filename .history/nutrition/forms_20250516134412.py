from django import forms
from .models import GoalRecommendation

class GoalSelectionForm(forms.Form):
    goal_type = forms.ChoiceField(
        choices=GoalRecommendation.GOAL_CHOICES,
        widget=forms.Select(attrs={'class': 'w-full p-2 border rounded'})
    )
