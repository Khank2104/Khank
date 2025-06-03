from django.db import migrations

def insert_goal_data(apps, schema_editor):
    GoalRecommendation = apps.get_model('nutrition', 'GoalRecommendation')
    data = [
        # BMI 15–19
        ('weight_loss', 15, 19, 1800, 200, 80, 50),
        ('muscle_gain', 15, 19, 1900, 220, 100, 60),
        ('maintenance', 15, 19, 2000, 210, 90, 55),
        ('energy', 15, 19, 2100, 230, 85, 65),
        # BMI 20–23
        ('weight_loss', 20, 23, 1600, 180, 70, 45),
        ('muscle_gain', 20, 23, 2200, 250, 110, 70),
        ('maintenance', 20, 23, 2100, 230, 95, 60),
        ('energy', 20, 23, 2300, 260, 90, 75),
        # BMI 24–27
        ('weight_loss', 24, 27, 1500, 160, 75, 40),
        ('muscle_gain', 24, 27, 2000, 230, 105, 65),
        ('maintenance', 24, 27, 1900, 220, 90, 55),
        ('energy', 24, 27, 2100, 240, 95, 70),
    ]
    for goal_type, bmi_min, bmi_max, cal, carb, prot, fat in data:
        GoalRecommendation.objects.create(
            goal_type=goal_type,
            bmi_min=bmi_min,
            bmi_max=bmi_max,
            calories=cal,
            carbs=carb,
            protein=prot,
            fat=fat,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '003_insert_goal_data.py'),  # hoặc 0002 nếu bạn không merge
    ]

    operations = [
        migrations.RunPython(insert_goal_data),
    ]
