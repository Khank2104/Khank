from django import forms

class GoalSelectionForm(forms.Form):
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('maintenance', 'Maintenance'),
        ('energy', 'Improve Energy'),
    ]
    goal_type = forms.ChoiceField(choices=GOAL_CHOICES, label='Health Goal')
