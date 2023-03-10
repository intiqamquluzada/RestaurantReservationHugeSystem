# Generated by Django 3.2 on 2023-03-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_delete_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Istifadəçi adı')),
                ('surname', models.CharField(blank=True, max_length=40, null=True, verbose_name='Istifadəçi soyadı')),
                ('pp', models.ImageField(blank=True, null=True, upload_to='accounts/')),
                ('slug', models.SlugField(unique=True)),
                ('activation_code', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('password_reset_code', models.CharField(blank=True, max_length=120, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'MyUser',
                'verbose_name_plural': 'MyUser',
                'ordering': ['-created_at'],
            },
        ),
    ]
