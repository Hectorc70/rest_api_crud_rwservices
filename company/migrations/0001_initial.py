# Generated by Django 3.1.6 on 2021-02-13 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('rfc', models.CharField(max_length=13, primary_key=True, serialize=False, unique=True, verbose_name='RFC')),
                ('name_company', models.CharField(max_length=100, verbose_name='Nombre de Empresa')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('street', models.CharField(max_length=300, verbose_name='Calle')),
                ('number_ext', models.CharField(max_length=40, verbose_name='Numero Exterior')),
                ('number_int', models.CharField(max_length=40, verbose_name='Numero Interior')),
                ('suburb', models.CharField(max_length=300, verbose_name='Colonia')),
                ('postal_code', models.IntegerField(verbose_name='Codigo Postal')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified', models.DateField(auto_now=True, verbose_name='Fecha de ultima Modificacion')),
                ('created_by', models.CharField(max_length=10, null=True, verbose_name='Creado Por')),
                ('modified_by', models.CharField(max_length=10, null=True, verbose_name='Modificado Por')),
                ('path_logo', models.CharField(max_length=500, null=True, verbose_name='Ruta Logo Imagen')),
            ],
        ),
    ]
