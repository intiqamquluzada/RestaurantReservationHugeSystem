# Generated by Django 3.2 on 2023-03-10 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0068_restaurants_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likers',
        ),
    ]
