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
