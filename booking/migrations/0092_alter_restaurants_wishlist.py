# Generated by Django 3.2 on 2023-03-22 20:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0091_restaurants_has_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='wishlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
