from django.db import models

# Create your models here.
class centrosBip(models.Model):
    linea = models.CharField(max_length=100)
    estacion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    este = models.FloatField(null=True)
    norte = models.FloatField(null=True)
    longitud = models.FloatField()
    latitud = models.FloatField()
