# Generated by Django 5.2 on 2025-05-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0003_savedexerciseplan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedexerciseplan',
            name='suggestions',
        ),
        migrations.AlterField(
            model_name='savedexerciseplan',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
    ]
