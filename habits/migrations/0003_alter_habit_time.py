# Generated by Django 4.2.5 on 2023-10-10 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_habit_pleasant_habit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='time',
        ),
        migrations.AddField(
            model_name='habit',
            name='time',
            field=models.DateTimeField(),
        ),
    ]