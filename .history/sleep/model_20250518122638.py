from django.db import models
from django.conf import settings

class SleepRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()  # Người dùng chọn ngày ngủ
    sleep_time = models.TimeField()
    wake_time = models.TimeField()
    duration_hours = models.FloatField()
    quality = models.CharField(max_length=20)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.date}"
