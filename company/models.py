from django.db import models
from django.utils import timezone
# Create your models here.


class Company(models.Model):
    __name__ = 'Company'
    rfc = models.CharField('RFC', max_length=13, primary_key=True,
                            blank=False, unique=True
                            )
    name_company = models.CharField('Nombre de Empresa', blank=False,
                                    max_length=100
                                    )

    email       = models.EmailField('Correo Electronico', blank=False,)    
    street      = models.CharField('Calle', max_length=300, blank=False)  
    number_ext  = models.CharField('Numero Exterior', max_length=40, blank=False)  
    number_int  = models.CharField('Numero Interior', max_length=40, blank=True)  
    suburb      = models.CharField('Colonia', max_length=300, blank=False)
    postal_code = models.CharField('Codigo Postal', max_length=10, blank=False)

    creation_date   = models.DateField('Fecha de creacion', null=False, auto_now_add=timezone.now())
    modified        = models.DateField('Fecha de ultima Modificacion', null=False, auto_now=timezone.now())
    created_by      = models.CharField('Creado Por', max_length=10, null=True)
    modified_by     = models.CharField('Modificado Por', max_length=10, null=True)
    path_logo       = models.CharField('Ruta Logo Imagen', max_length=500, null=True)   

    def __str__(self):
        return self.name_company