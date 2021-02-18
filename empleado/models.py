from django.db import models
from django.utils import timezone


from users.models import NewUser
# Create your models here.


class Employee(models.Model):
    rfc = models.CharField('RFC', max_length=13, primary_key=True,
                            blank=False, unique=True
                            )
    name = models.CharField('Nombre de Empleado', blank=False,
                                    max_length=100
                                    )
    second_name = models.CharField('Segundo nombre', blank=True, null=True,
                                    max_length=100
                                    )

    last_name = models.CharField('Apellido Paterno', blank=False,
                                    max_length=100
                                    ) 
    
    second_last_name = models.CharField('Apellido Materno', blank=False,
                                    max_length=100
                                    ) 

    curp = models.CharField('CURP', blank=False,
                                    max_length=100
                                    ) 
    birthday = models.DateField('Fecha de Nacimiento', blank=False)
    email       = models.EmailField('Correo Electronico', blank=False,)    
    

    creation_date   = models.DateField('Fecha de creacion', null=False, auto_now_add=timezone.now())
    modified        = models.DateField('Fecha de ultima Modificacion', null=False, auto_now=timezone.now())
    created_by      = models.CharField('Creado Por', max_length=10, null=True)
    modified_by     = models.CharField('Modificado Por', max_length=10, null=True)

    user            = models.ForeignKey(NewUser, blank=True, null=True, on_delete=models.CASCADE, related_name='user')


    class Meta:
        verbose_name = 'Empleado'

    def __str__(self):
        return self.name

        