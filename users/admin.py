
from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea


class UserAdminConfig(UserAdmin):
    model = NewUser



admin.site.register(NewUser, UserAdminConfig)