# Generated by Django 4.1.2 on 2022-12-20 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fmc', '0012_appliance'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliance',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appliance_to_service', to='fmc.work'),
        ),
    ]
