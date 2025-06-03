from django.db import migrations

def insert_suggested_meals(apps, schema_editor):
    SuggestedMeal = apps.get_model('nutrition', 'SuggestedMeal')
    data = [
        ('weight_loss', 15, 19, 'breakfast', 'Oatmeal with Berries', 250, 35, 10, 5),
        ('weight_loss', 15, 19, 'lunch', 'Grilled Chicken Salad', 400, 30, 35, 15),
        ('weight_loss', 15, 19, 'dinner', 'Steamed Veggies with Tofu', 450, 40, 25, 20),
        ('weight_loss', 15, 19, 'snack', 'Apple with Peanut Butter', 200, 25, 5, 10),

        ('muscle_gain', 20, 23, 'breakfast', 'Eggs and Whole Grain Toast', 400, 30, 25, 15),
        ('muscle_gain', 20, 23, 'lunch', 'Beef Stir Fry with Rice', 600, 50, 35, 25),
        ('muscle_gain', 20, 23, 'dinner', 'Grilled Salmon with Quinoa', 700, 45, 40, 30),
        ('muscle_gain', 20, 23, 'snack', 'Protein Shake', 300, 20, 30, 10),
    ]

    for goal, bmi_min, bmi_max, meal_type, name, cal, carb, prot, fat in data:
        SuggestedMeal.objects.create(
            goal_type=goal,
            bmi_min=bmi_min,
            bmi_max=bmi_max,
            meal_type=meal_type,
            meal_name=name,
            calories=cal,
            carbs=carb,
            protein=prot,
            fat=fat,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0005_suggestedmeal'),
    ]

    operations = [
        migrations.RunPython(insert_suggested_meals),
    ]
