# Generated by Django 3.1.6 on 2021-03-31 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_auto_20210327_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='created_by',
            field=models.CharField(default=' ', max_length=10, verbose_name='Creado Por'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='modified_by',
            field=models.CharField(default=' ', max_length=10, verbose_name='Modificado Por'),
            preserve_default=False,
        ),
    ]
