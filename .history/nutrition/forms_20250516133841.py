from django import forms


class UserGoalForm(forms.ModelForm):
    class Meta:
        model = UserGoal
        fields = ['goal_type', 'calorie_target', 'carbs', 'protein', 'fat']
