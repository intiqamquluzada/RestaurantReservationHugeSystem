# Generated by Django 3.2 on 2023-03-29 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0102_alter_restaurants_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='opened',
            field=models.TimeField(blank=True, default='None', null=True),
        ),
    ]
