# Generated by Django 3.2 on 2023-02-20 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_blogmodel_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'ordering': ('-created_at',), 'verbose_name': 'Blog Model', 'verbose_name_plural': 'Blog models'},
        ),
    ]
