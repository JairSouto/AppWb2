from calendar import c
from errno import EADDRNOTAVAIL
from django.db import models

# Create your models here.
class Empleados(models.Model):
    nombre = models.CharField(max_length=40)
    grupo = models.IntegerField()
    fechaDeRegistro= models.DateField()
    salario = models.IntegerField()
    email= models.EmailField()
class TiposDTrabajo(models.Model):
    ocupacion = models.CharField(max_length=30)
    horas_d_empleo = models.IntegerField()
    edadEnElTrabajo = models.IntegerField()
class TipoDmaterial(models.Model):
    material = models.CharField(max_length=50)
    peso = models.IntegerField()


  



