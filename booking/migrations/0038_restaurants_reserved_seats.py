# Generated by Django 3.2 on 2023-02-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0037_remove_restaurants_available_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='reserved_seats',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
