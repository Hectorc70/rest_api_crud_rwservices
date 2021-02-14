from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager, PermissionsMixin

from django.utils import timezone


from company.models import Company

# Create your models here.
class CustomUserManager(BaseUserManager):
    """ 
    Administrador de modelo de usuario personalizado donde el Numero de telefono
    es el identificador único para la autenticación en lugar de los nombres de usuario 
    """ 

    def create_user(self, id_user, password, **extra_fields):
        if not id_user:
            raise ValueError(_('Escriba un numero de usuario(Numero de telefono)'))
        
        id_user = self.normalize_email(id_user)
        user = self.model(id_user=id_user)

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, id_user, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(id_user, password, **extra_fields)



class NewUser(AbstractUser):

    
    id_user       = models.CharField('id usuario', max_length=10,unique=True, null=False)
    ocuppied_by  = models.ForeignKey(Company, blank=True, null=True,on_delete=models.DO_NOTHING, related_name='cliente_empresa')
    
    creation_date = models.DateTimeField('Fecha de Creacion', editable=False, null=True)
    modified      = models.DateTimeField('Modificado', null=True)
    created_by    = models.CharField('Creado Por', max_length=10, null=True)
    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'id_user'

    # requerido para superuser
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.id_user:
            self.creation_date = timezone.now()

        self.modified = timezone.now()

        return super(NewUser, self).save(*args, **kwargs)



    def __str__(self):
        return self.id_user
