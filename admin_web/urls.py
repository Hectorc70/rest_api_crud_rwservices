app_name = 'admin_web'
from django.urls import path, include
from .views import *
urlpatterns = [
    path('login/', ingresar, name='login'),
] 