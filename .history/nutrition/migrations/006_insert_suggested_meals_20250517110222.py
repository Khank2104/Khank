from django.db import migrations

def insert_suggested_meals(apps, schema_editor):
    SuggestedMeal = apps.get_model('nutrition', 'SuggestedMeal')
    data = [
       # Weight Loss
    ('weight_loss', 15, 19, 'breakfast', 'Oatmeal with Berries', 250, 35, 10, 5),
    ('weight_loss', 15, 19, 'lunch', 'Grilled Chicken Salad', 400, 30, 35, 15),
    ('weight_loss', 15, 19, 'dinner', 'Steamed Veggies with Tofu', 450, 40, 25, 20),
    ('weight_loss', 15, 19, 'snack', 'Apple with Peanut Butter', 200, 25, 5, 10),
    
    ('weight_loss', 20, 23, 'breakfast', 'Greek Yogurt with Honey', 200, 25, 15, 5),
    ('weight_loss', 20, 23, 'lunch', 'Turkey Wrap with Veggies', 350, 30, 25, 10),
    ('weight_loss', 20, 23, 'dinner', 'Baked Cod with Spinach', 450, 35, 30, 15),
    ('weight_loss', 20, 23, 'snack', 'Carrot Sticks with Hummus', 150, 15, 5, 7),
    
    ('weight_loss', 24, 27, 'breakfast', 'Smoothie with Spinach and Banana', 180, 30, 10, 3),
    ('weight_loss', 24, 27, 'lunch', 'Grilled Chicken with Broccoli', 400, 25, 35, 10),
    ('weight_loss', 24, 27, 'dinner', 'Zucchini Noodles with Pesto', 420, 30, 20, 15),
    ('weight_loss', 24, 27, 'snack', 'Low-fat Cottage Cheese', 160, 10, 15, 4),

    # Muscle Gain
    ('muscle_gain', 15, 19, 'breakfast', 'Peanut Butter Toast with Banana', 400, 40, 20, 15),
    ('muscle_gain', 15, 19, 'lunch', 'Chicken Burrito Bowl', 600, 50, 35, 20),
    ('muscle_gain', 15, 19, 'dinner', 'Beef and Sweet Potato', 650, 45, 40, 25),
    ('muscle_gain', 15, 19, 'snack', 'Trail Mix', 300, 30, 10, 15),

    ('muscle_gain', 20, 23, 'breakfast', 'Eggs and Whole Grain Toast', 400, 30, 25, 15),
    ('muscle_gain', 20, 23, 'lunch', 'Beef Stir Fry with Rice', 600, 50, 35, 25),
    ('muscle_gain', 20, 23, 'dinner', 'Grilled Salmon with Quinoa', 700, 45, 40, 30),
    ('muscle_gain', 20, 23, 'snack', 'Protein Shake', 300, 20, 30, 10),

    ('muscle_gain', 24, 27, 'breakfast', 'Omelette with Cheese and Avocado', 500, 25, 30, 35),
    ('muscle_gain', 24, 27, 'lunch', 'Chicken Alfredo Pasta', 700, 55, 45, 30),
    ('muscle_gain', 24, 27, 'dinner', 'Pork Chops with Mashed Potatoes', 750, 50, 40, 35),
    ('muscle_gain', 24, 27, 'snack', 'Granola Bar and Milk', 350, 40, 15, 12),

    # Maintenance
    ('maintenance', 15, 19, 'breakfast', 'Yogurt Parfait with Granola', 300, 40, 15, 8),
    ('maintenance', 15, 19, 'lunch', 'Chicken Caesar Wrap', 500, 35, 30, 18),
    ('maintenance', 15, 19, 'dinner', 'Pasta Primavera', 550, 50, 20, 15),
    ('maintenance', 15, 19, 'snack', 'Fruit Salad', 200, 30, 2, 2),

    ('maintenance', 20, 23, 'breakfast', 'Scrambled Eggs with Toast', 350, 30, 20, 10),
    ('maintenance', 20, 23, 'lunch', 'Teriyaki Chicken with Rice', 550, 45, 35, 15),
    ('maintenance', 20, 23, 'dinner', 'Grilled Shrimp and Couscous', 600, 40, 30, 18),
    ('maintenance', 20, 23, 'snack', 'Greek Yogurt', 180, 15, 12, 5),

    ('maintenance', 24, 27, 'breakfast', 'Bagel with Cream Cheese and Fruit', 400, 45, 12, 15),
    ('maintenance', 24, 27, 'lunch', 'Ham Sandwich and Salad', 550, 40, 25, 20),
    ('maintenance', 24, 27, 'dinner', 'Stir Fry with Tofu', 600, 50, 20, 15),
    ('maintenance', 24, 27, 'snack', 'Boiled Eggs and Crackers', 220, 15, 10, 8),

    # Energy
    ('energy', 15, 19, 'breakfast', 'Fruit Smoothie and Toast', 350, 50, 10, 8),
    ('energy', 15, 19, 'lunch', 'Rice and Chicken Curry', 600, 55, 25, 18),
    ('energy', 15, 19, 'dinner', 'Grilled Tuna and Brown Rice', 650, 45, 35, 20),
    ('energy', 15, 19, 'snack', 'Banana with Almond Butter', 250, 30, 5, 10),

    ('energy', 20, 23, 'breakfast', 'Peanut Butter Banana Oatmeal', 400, 45, 15, 12),
    ('energy', 20, 23, 'lunch', 'Pasta with Tomato and Chicken', 650, 55, 30, 20),
    ('energy', 20, 23, 'dinner', 'Stuffed Bell Peppers', 700, 50, 35, 25),
    ('energy', 20, 23, 'snack', 'Fruit and Nut Mix', 280, 35, 8, 12),

    ('energy', 24, 27, 'breakfast', 'Chia Pudding with Mango', 420, 50, 12, 15),
    ('energy', 24, 27, 'lunch', 'Tuna Sandwich with Corn Soup', 600, 50, 25, 20),
    ('energy', 24, 27, 'dinner', 'Couscous with Roasted Chicken', 750, 60, 35, 25),
    ('energy', 24, 27, 'snack', 'Peanut Bar and Milk', 320, 30, 10, 15),   
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
