# Generated by Django 4.1.2 on 2022-12-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmc', '0030_alter_appliances_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='part',
        ),
        migrations.AddField(
            model_name='appliances',
            name='part',
            field=models.ManyToManyField(blank=True, related_name='add_part', to='fmc.work'),
        ),
    ]
