# Generated by Django 4.1.2 on 2022-12-21 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fmc', '0022_alter_work_address_parts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='address_parts',
            new_name='product',
        ),
    ]
