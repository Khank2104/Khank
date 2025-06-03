from django import forms

class GoalSelectionForm(forms.Form):
    goal_type = forms.ChoiceField(choices=[
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('maintenance', 'Maintenance'),
        ('energy', 'Improve Energy')
    ])
