# Generated by Django 3.2 on 2023-02-23 20:41

from django.db import migrations, models
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0019_auto_20230224_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantmenu',
            name='images',
            field=models.FileField(upload_to=services.uploader.Uploader.upload_menu_to_restaurants),
        ),
    ]
