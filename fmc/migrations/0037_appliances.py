# Generated by Django 4.1.2 on 2022-12-28 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fmc', '0036_remove_work_part_delete_appliances'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appliance', models.CharField(max_length=64, null=64)),
                ('part_name', models.CharField(max_length=64, null=True)),
                ('model_number', models.CharField(max_length=64, null=True)),
                ('part_number', models.CharField(max_length=64, null=True)),
                ('url', models.URLField(null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appliances', to='fmc.work')),
            ],
        ),
    ]
