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



#test

class SuggestedMeal(models.Model):
    MEAL_TYPE_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('maintenance', 'Maintenance'),
        ('energy', 'Improve Energy'),
    ]

    goal_type = models.CharField(max_length=20, choices=GOAL_CHOICES)
    bmi_min = models.FloatField()
    bmi_max = models.FloatField()
    meal_type = models.CharField(max_length=10, choices=MEAL_TYPE_CHOICES)
    meal_name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.meal_type}: {self.meal_name} ({self.goal_type})"



class FoodEntry(models.Model):
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=10, choices=MEAL_CHOICES)
    food_item = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.food_item} ({self.user.email}) - {self.date}"