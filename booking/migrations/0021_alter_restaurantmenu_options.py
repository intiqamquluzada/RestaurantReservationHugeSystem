# Generated by Django 3.2 on 2023-02-23 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0020_alter_restaurantmenu_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurantmenu',
            options={'ordering': ('-created_at',), 'verbose_name': 'Menu', 'verbose_name_plural': 'Menus'},
        ),
    ]