# Generated by Django 4.1.2 on 2022-12-27 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fmc', '0034_work_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='slug',
        ),
    ]
