# Generated by Django 3.2 on 2023-03-24 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0096_auto_20230325_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='user',
        ),
    ]
