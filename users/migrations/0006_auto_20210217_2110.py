# Generated by Django 3.1.6 on 2021-02-18 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20210217_2056'),
        ('users', '0005_auto_20210217_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='type_obj',
            field=models.CharField(default='U', max_length=1, verbose_name='Tipo de Objeto'),
        ),
        migrations.AddField(
            model_name='rol',
            name='type_obj',
            field=models.CharField(default='R', max_length=1, verbose_name='Tipo de Objeto'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='creation_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='occupied_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cliente_empresa', to='company.company', verbose_name='Ocupado por la Empresa'),
        ),
    ]