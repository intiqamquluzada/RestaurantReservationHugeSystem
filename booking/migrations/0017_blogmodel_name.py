# Generated by Django 3.2 on 2023-02-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_blogmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='name',
            field=models.CharField(default='e', max_length=200),
            preserve_default=False,
        ),
    ]
