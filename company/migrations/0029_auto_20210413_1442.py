# Generated by Django 3.0.2 on 2021-04-13 19:42

from django.db import migrations, models
import rest_api_crud_rwservices.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0028_auto_20210413_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictureactivity',
            name='img_file',
            field=models.ImageField(storage=rest_api_crud_rwservices.storage_backends.PublicMediaStorage(), upload_to=''),
        ),
    ]
