from django.db import models
from django.conf import settings

class WaterIntake(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    amount_ml = models.PositiveIntegerField()
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.date} {self.time} - {self.amount_ml}ml"
