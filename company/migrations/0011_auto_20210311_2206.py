# Generated by Django 3.1.6 on 2021-03-12 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20210311_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Tarea', 'verbose_name_plural': 'Tareas'},
        ),
        migrations.RemoveField(
            model_name='activity',
            name='path_img_header',
        ),
        migrations.AlterField(
            model_name='task',
            name='name_task',
            field=models.CharField(max_length=100, null=True, verbose_name='Nombre de Tarea Realizada'),
        ),
    ]
