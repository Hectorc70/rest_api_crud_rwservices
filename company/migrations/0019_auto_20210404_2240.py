# Generated by Django 3.1.6 on 2021-04-05 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0018_auto_20210330_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='observations',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones de Actividad'),
        ),
    ]
