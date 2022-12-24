# Generated by Django 4.1.2 on 2022-12-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmc', '0011_remove_work_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.CharField(blank=True, max_length=64)),
                ('part_model', models.CharField(max_length=64, null=True)),
                ('part_number', models.CharField(blank=True, max_length=64)),
                ('url', models.URLField(null=True)),
            ],
        ),
    ]
