# Generated by Django 5.2.1 on 2025-05-21 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_gender_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_weight_update',
            field=models.DateField(blank=True, null=True),
        ),
    ]
