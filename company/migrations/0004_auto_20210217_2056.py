# Generated by Django 3.1.6 on 2021-02-18 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_activity_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='Company',
            new_name='company',
        ),
    ]
