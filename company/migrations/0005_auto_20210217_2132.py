# Generated by Django 3.1.6 on 2021-02-18 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20210217_2056'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='activity',
            table='Actividad',
        ),
        migrations.AlterModelTable(
            name='company',
            table='Empresa',
        ),
    ]