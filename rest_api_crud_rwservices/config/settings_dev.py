
import os
import configparser
config = configparser.ConfigParser()
config.read("config.ini")

ALLOWED_HOSTS = ['127.0.0.1']
SECRET_KEY = config['DEV']['SECRET_KEY']

DEBUG = True



DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.postgresql',
            'NAME':config['PROD']['DB_NAME'],
            'USER':config['PROD']['DB_USER'],
            'PASSWORD': config['PROD']['DB_PASSWORD'],
            'HOST': config['PROD']['DB_HOST'],
            'PORT': config['PROD']['DB_PORT'],
        }
}

AWS_ACCESS_KEY_ID = config['DEV_AWS']['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = config['DEV_AWS']['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = config['DEV_AWS']['AWS_STORAGE_BUCKET_NAME']