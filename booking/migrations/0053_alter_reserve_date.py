# Generated by Django 3.2 on 2023-03-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0052_auto_20230306_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='date',
            field=models.TimeField(),
        ),
    ]
