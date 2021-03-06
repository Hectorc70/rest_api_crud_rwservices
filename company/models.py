from django.db import models
from django.utils import timezone
from django.conf import settings

from rest_api_crud_rwservices.storage_backends import PrivateMediaStorage, PublicMediaStorage
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
    path_logo       = models.CharField('Ruta Logo Imagen', max_length=500, null=True, blank=True)   

    class Meta:
        verbose_name = 'Empresa'

    def __str__(self):
        return "RFC: {} \t Nombre: {}".format(self.rfc, self.name_company)



class Area(models.Model):

    id_area         = models.AutoField(primary_key=True, unique=True)
    name_area       = models.CharField('Nombre de Area', max_length=300)
    path_img_header = models.ImageField(storage=PrivateMediaStorage())

    creation_date   = models.DateField('Fecha de creacion', null=False, auto_now_add=timezone.now())
    modified        = models.DateField('Fecha de ultima Modificacion', null=False, auto_now=timezone.now())
    created_by      = models.CharField('Creado Por', max_length=10, null=True)
    modified_by     = models.CharField('Modificado Por', max_length=10, null=True)

    company         = models.ForeignKey(Company, null=False, on_delete=models.CASCADE, related_name='company')


    class Meta:
        verbose_name = 'Area'

    def __str__(self):
        return self.name_area



class Activity(models.Model):


    id_activity     = models.AutoField(primary_key=True, unique=True)
    name_activity   = models.CharField('Nombre de Actividad', max_length=300)
    status          = models.BooleanField('Estatus')    
    observations    = models.TextField('Observaciones de Actividad', blank=True, null=True)
    
    creation_date   = models.DateField('Fecha de creacion', null=False, auto_now_add=timezone.now())
    created_by      = models.CharField('Creado Por', max_length=10, null=False)
    modified        = models.DateField('Fecha de ultima Modificacion', null=False, auto_now=timezone.now())
    modified_by     = models.CharField('Modificado Por', max_length=10, null=False)

    area         = models.ForeignKey(Area, null=False, on_delete=models.CASCADE, related_name='area')
    

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return self.name_activity

    
class Picture(models.Model):

    id_img          = models.AutoField(primary_key=True, unique=True)
    tipo_img        = models.CharField('tipo', max_length=100)
    img_file        = models.ImageField(storage=PrivateMediaStorage())
    
    creation_date   = models.DateField('Fecha de creacion', null=False, auto_now_add=timezone.now())
    created_by      = models.CharField('Creado Por', max_length=10, null=True)
    modified        = models.DateField('Fecha de ultima Modificacion', null=False, auto_now=timezone.now())
    modified_by     = models.CharField('Modificado Por', max_length=10, null=True)

    activity         = models.ForeignKey(Activity, null=False, on_delete=models.CASCADE, related_name='activity_pictures')
    

    class Meta:
        verbose_name = 'imagen Actividad'
        verbose_name_plural = 'imagenes'

    def __str__(self):
        return self.tipo_img



class Task(models.Model):
    id_task       = models.AutoField(primary_key=True, unique=True)    
    name_task  = models.CharField('Nombre de Tarea Realizada', max_length=100, null=True)
    
    creation_date   = models.DateField('Fecha de creacion', null=False, auto_now_add=timezone.now())
    created_by      = models.CharField('Creado Por', max_length=10, null=True)
    modified        = models.DateField('Fecha de ultima Modificacion', null=False, auto_now=timezone.now())
    modified_by     = models.CharField('Modificado Por', max_length=10, null=True)

    activity     = models.ForeignKey(Activity, null=False, on_delete=models.CASCADE, related_name='activity_tarea')


    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return self.name_task


