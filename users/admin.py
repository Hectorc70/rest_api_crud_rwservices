
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import(
    CustomUserChangeForm,
    CustomUserCreationForm
)

from users.models import(
    NewUser,
    Rol
)




class CustomUserAdmin(UserAdmin):
    form     = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = UserAdmin.fieldsets+ (
        (
            None,{
            'fields':(
                'id_user',
                'occupied_by',    
                'creation_date',
                'modified',    
                'created_by',  
                'rol'
                )
            }
        ),
    )

@admin.register(NewUser)
class UserAdmin(CustomUserAdmin):
    list_display=(
        'id_user',      
        'password',
        'is_staff',
        'is_active',
        'is_superuser',        
        'occupied_by',    
        'creation_date',
        'modified',    
        'created_by',  
        'rol',
        'last_login',
        'date_joined'

    )




@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = (
        'id_rol',
        'name_rol',
    )