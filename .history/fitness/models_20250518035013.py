from django.db import models
from django.conf import settings

class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    date = models.DateField()

class ExerciseSuggestion(models.Model):
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

    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    bmi_min = models.FloatField()
    bmi_max = models.FloatField()
    name = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    calories_burned = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.goal}, {self.level})"



