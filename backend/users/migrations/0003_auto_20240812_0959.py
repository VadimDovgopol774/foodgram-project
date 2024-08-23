# Generated by Django 3.2.3 on 2024-08-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20240729_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=250, unique=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='Имя пользователя'),
        ),
    ]
