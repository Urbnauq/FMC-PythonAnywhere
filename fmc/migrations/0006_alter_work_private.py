# Generated by Django 4.1.2 on 2022-12-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmc', '0005_alter_work_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='private',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=12),
        ),
    ]
