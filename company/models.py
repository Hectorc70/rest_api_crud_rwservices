from django.db import models
from django.utils import timezone
# Create your models here.


class Company(models.Model):
    
    
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

    class Meta:
        verbose_name = 'Empresa'

    def __str__(self):
        return self.name_company



class Area(models.Model):

    id_area         = models.AutoField(primary_key=True, unique=True)
    name_area       = models.CharField('Nombre de Area', max_length=300)
    creation_date   = models.DateField('Fecha de creacion', null=False, auto_now_add=timezone.now())
    modified        = models.DateField('Fecha de ultima Modificacion', null=False, auto_now=timezone.now())
    created_by      = models.CharField('Creado Por', max_length=10, null=True)
    modified_by     = models.CharField('Modificado Por', max_length=10, null=True)
    path_img_header = models.CharField('Ruta de Imagen de Header', max_length=300, null=True)

    company         = models.ForeignKey(Company, null=False, on_delete=models.CASCADE, related_name='company')


    class Meta:
        verbose_name = 'Area'

    def __str__(self):
        return self.name_area



class Activity(models.Model):


    id_activity     = models.AutoField(primary_key=True, unique=True)
    name_activity   = models.CharField('Nombre de Actividad', max_length=300)
    status          = models.BooleanField('Estatus')    
    observations    = models.TextField('Observaciones de Actividad')
    path_img_header = models.CharField('Ruta de Imagen de Header', max_length=300, null=True)
    
    creation_date   = models.DateField('Fecha de creacion', null=False, auto_now_add=timezone.now())
    created_by      = models.CharField('Creado Por', max_length=10, null=True)
    modified        = models.DateField('Fecha de ultima Modificacion', null=False, auto_now=timezone.now())
    modified_by     = models.CharField('Modificado Por', max_length=10, null=True)

    area         = models.ForeignKey(Area, null=False, on_delete=models.CASCADE, related_name='Area')
    

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return self.name_activity

        