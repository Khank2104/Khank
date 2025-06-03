from django import forms



class ExerciseFilterForm(forms.Form):
    GOAL_CHOICES = [
        ('fat_loss', 'Fat Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('endurance', 'Endurance'),
        ('flexibility', 'Flexibility'),
        ('fitness', 'General Fitness'),
    ]

    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    goal = forms.ChoiceField(choices=GOAL_CHOICES)
    level = forms.ChoiceField(choices=LEVEL_CHOICES)
    duration = forms.IntegerField(min_value=1)
