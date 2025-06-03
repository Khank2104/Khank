from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from fitness.models import Activity, ExerciseSuggestion, SavedExercisePlan
from hydration.models import WaterIntake
from nutrition.models import GoalRecommendation, SavedMealPlan, SuggestedMeal, FoodEntry
from sleep.models import SleepRecord
from accounts.models import User  # User thì vẫn đúng

admin.site.register(User, UserAdmin)

admin.site.register(Activity)
admin.site.register(ExerciseSuggestion)
admin.site.register(SavedExercisePlan)
admin.site.register(WaterIntake)
admin.site.register(GoalRecommendation)
admin.site.register(SavedMealPlan)
admin.site.register(SuggestedMeal)
admin.site.register(FoodEntry)
admin.site.register(SleepRecord)