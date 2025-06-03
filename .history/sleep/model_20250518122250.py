from django.db import models
from django.conf import settings

class SleepLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    sleep_time = models.TimeField()
    wake_time = models.TimeField()
    duration_hours = models.FloatField()
    quality = models.CharField(max_length=20)
    notes = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.date}"
