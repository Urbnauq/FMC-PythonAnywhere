# Generated by Django 4.1.2 on 2022-12-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmc', '0007_work_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('2C2R', '2C2R'), ('Completed', 'Completed')], default='Pending', max_length=12),
        ),
    ]
