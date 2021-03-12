# Generated by Django 3.1.6 on 2021-03-10 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20210224_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenActividad',
            fields=[
                ('id_img', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name_img', models.CharField(max_length=300, verbose_name='Nombre de Imagen')),
                ('tipo', models.CharField(max_length=300, verbose_name='tipo')),
                ('path_img', models.CharField(max_length=500, null=True, verbose_name='Ruta de Imagen de Header')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('created_by', models.CharField(max_length=10, null=True, verbose_name='Creado Por')),
                ('modified', models.DateField(auto_now=True, verbose_name='Fecha de ultima Modificacion')),
                ('modified_by', models.CharField(max_length=10, null=True, verbose_name='Modificado Por')),
                ('Activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Activity', to='company.activity')),
            ],
            options={
                'verbose_name': 'imagen Actividad',
                'verbose_name_plural': 'imagenes',
            },
        ),
    ]
