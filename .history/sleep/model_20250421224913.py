from django.db import models
from django.conf import settings


class SleepRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sleep_time = models.TimeField()
    wake_time = models.TimeField()
    duration_hours = models.FloatField()
    quality = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    note = models.TextField(blank=True)
