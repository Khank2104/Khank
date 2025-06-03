from django import forms
from .models import SleepRecord

class SleepRecordForm(forms.ModelForm):
    class Meta:
        model = SleepRecord
        fields = ['date', 'sleep_time', 'wake_time', 'quality', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'sleep_time': forms.TimeInput(attrs={'type': 'time'}),
            'wake_time': forms.TimeInput(attrs={'type': 'time'}),
            'duration_hours': forms.NumberInput(attrs={'step': 0.1}),
        }
