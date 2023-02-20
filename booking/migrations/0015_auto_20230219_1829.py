# Generated by Django 3.2 on 2023-02-19 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_restaurants_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='available_seats',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='type_r',
            field=models.CharField(choices=[('Fast-food', 'Fast-food'), ('Milli', 'Milli'), ('Ailəvi', 'Ailəvi'), ('Business-lunch', 'Business-lunch'), ('Şirniyyat', 'Şirniyyat'), ('Vegetarian', 'Vegetarian'), ('Özünə xidmət', 'Özünə xidmət'), ('Klub', 'Klub')], max_length=100),
        ),
    ]