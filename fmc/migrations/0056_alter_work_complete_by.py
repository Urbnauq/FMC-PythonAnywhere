# Generated by Django 4.0.6 on 2023-02-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmc', '0055_alter_work_complete_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='complete_by',
            field=models.CharField(blank=True, choices=[('', '-------'), ('Canela', 'Canela'), ('Eddie', 'Eddie'), ('Jansel', 'Jansel'), ('Jose', 'Jose'), ('Luis', 'Luis'), ('Oscar A.', 'Oscar A.'), ('Oscar', 'Oscar')], default='', max_length=12, verbose_name='Complete By'),
        ),
    ]
