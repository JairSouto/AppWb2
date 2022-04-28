
from django.db import models

# Create your models here.
class Equipos(models.Model):
    nombre = models.CharField(max_length=40)
    
    fechaDeRegistro= models.DateField()

    seguidores = models.IntegerField()

    
class Asociados(models.Model):
    nombre = models.CharField(max_length=40)
    Redes_Sociales = models.CharField(max_length=120)

class Cursos(models.Model):
    nombre = models.CharField(max_length=70)
    jugadorPro = models.CharField(max_length=70)
    Duracion = models.CharField(max_length=50)



  



