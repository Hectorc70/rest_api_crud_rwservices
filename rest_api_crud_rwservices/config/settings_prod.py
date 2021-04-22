
import django_heroku
import os
from decouple import config
import dj_database_url


ALLOWED_HOSTS = ['rwapi.herokuapp.com']
SECRET_KEY = config('SECRET_KEY')

DEBUG = True


DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )

    
}

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')