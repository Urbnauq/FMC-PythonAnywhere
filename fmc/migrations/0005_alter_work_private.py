# Generated by Django 4.1.2 on 2022-12-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmc', '0004_alter_work_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='private',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=12),
        ),
    ]
