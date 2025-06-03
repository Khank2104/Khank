from django.db import models
from django.conf import settings

class NutritionEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=20)
    food_item = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    carbohydrates = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

class SuggestedMeal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=20)
    description = models.TextField()
    calories = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()
    generated_on = models.DateField(auto_now_add=True)
