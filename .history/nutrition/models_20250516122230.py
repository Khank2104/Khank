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

class SuggestedMealPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class SuggestedMeal(models.Model):
    plan = models.ForeignKey(SuggestedMealPlan, on_delete=models.CASCADE, related_name='meals')
    meal_type = models.CharField(max_length=20)
    description = models.TextField()
    calories = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()



class WeightLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.weight}kg at {self.recorded_at}"

