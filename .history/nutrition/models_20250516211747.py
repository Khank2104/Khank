from django.db import models

class GoalRecommendation(models.Model):
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('maintenance', 'Maintenance'),
        ('energy', 'Improve Energy'),
    ]

    goal_type = models.CharField(max_length=20, choices=GOAL_CHOICES)
    bmi_min = models.FloatField()
    bmi_max = models.FloatField()
    calories = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.goal_type} (BMI {self.bmi_min}-{self.bmi_max})"

from django.conf import settings

class SavedMealPlan(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=20, choices=GoalRecommendation.GOAL_CHOICES)
    calorie_target = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()

    def __str__(self):
        return f"SavedPlan for {self.user.email}"
