# Generated by Django 3.2 on 2023-02-28 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0038_restaurants_reserved_seats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurants',
            old_name='reserved_seats',
            new_name='available_seats',
        ),
    ]