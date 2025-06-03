from django import forms
from .models import GoalRecommendation

class GoalSelectionForm(forms.Form):
    goal_type = forms.ChoiceField(
        choices=GoalRecommendation.GOAL_CHOICES,
        widget=forms.Select(attrs={'class': 'w-full p-2 border rounded'})
    )


from django import forms

class GoalSelectionForm(forms.Form):
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('maintenance', 'Maintenance'),
        ('energy', 'Improve Energy'),
    ]
    goal_type = forms.ChoiceField(choices=GOAL_CHOICES, label='Health Goal')
