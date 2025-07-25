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


class UserGoal(models.Model):
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('maintenance', 'Maintenance'),
        ('energy', 'Improve Energy'),
    ]

    DIET_CHOICES = [
        ('none', 'No Restrictions'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('low_carb', 'Low-Carb'),
        ('gluten_free', 'Gluten-Free'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=20, choices=GOAL_CHOICES)
    calorie_target = models.PositiveIntegerField()
    diet_preference = models.CharField(max_length=20, choices=DIET_CHOICES, default='none')
    carb_ratio = models.PositiveIntegerField(default=50)
    protein_ratio = models.PositiveIntegerField(default=30)
    fat_ratio = models.PositiveIntegerField(default=20)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.get_goal_type_display()}"
