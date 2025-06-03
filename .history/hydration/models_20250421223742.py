from django.db import models
from django.conf import settings

class WaterIntake(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount_ml = models.PositiveIntegerField()
    time = models.TimeField()
    date = models.DateField(auto_now_add=True)
    note = models.CharField(max_length=255, blank=True)
