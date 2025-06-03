from django.db import migrations

def insert_goal_data(apps, schema_editor):
    GoalRecommendation = apps.get_model('nutrition', 'GoalRecommendation')
    data = [
        (15, 19, 'weight_loss', 1800, 200, 80, 50),
        (15, 19, 'muscle_gain', 1900, 220, 100, 60),
        (15, 19, 'maintenance', 2000, 210, 90, 55),
        (15, 19, 'energy', 2100, 230, 85, 65),
        (20, 23, 'weight_loss', 1600, 180, 70, 45),
        (20, 23, 'muscle_gain', 2200, 250, 110, 70),
        (20, 23, 'maintenance', 2100, 230, 95, 60),
        (20, 23, 'energy', 2300, 260, 90, 75),
        (24, 27, 'weight_loss', 1500, 160, 75, 40),
        (24, 27, 'muscle_gain', 2000, 230, 105, 65),
        (24, 27, 'maintenance', 1900, 220, 90, 55),
        (24, 27, 'energy', 2100, 240, 95, 70),
    ]
    for bmi_min, bmi_max, goal, cal, carbs, protein, fat in data:
        GoalRecommendation.objects.create(
            bmi_min=bmi_min,
            bmi_max=bmi_max,
            goal_type=goal,
            calories=cal,
            carbs=carbs,
            protein=protein,
            fat=fat
        )

class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0001_initial'),  # nếu migration trước là 0001
    ]

    operations = [
        migrations.RunPython(insert_goal_data),
    ]
