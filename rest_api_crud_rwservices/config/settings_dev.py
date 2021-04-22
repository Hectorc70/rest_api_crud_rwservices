
import os
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
tipo = config['DEV']

ALLOWED_HOSTS = ['127.0.0.1']
SECRET_KEY = tipo['SECRET_KEY']

DEBUG = False



DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.postgresql',
            'NAME':tipo['DB_NAME'],
            'USER':tipo['DB_USER'],
            'PASSWORD': tipo['DB_PASSWORD'],
            'HOST': tipo['DB_HOST'],
            'PORT': tipo['DB_PORT'],
        }
}

AWS_ACCESS_KEY_ID = config['DEV_AWS']['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = config['DEV_AWS']['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = config['DEV_AWS']['AWS_STORAGE_BUCKET_NAME']