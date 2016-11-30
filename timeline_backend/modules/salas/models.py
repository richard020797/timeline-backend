from django.db import models

class Sala(models.Model):

    id_sala = models.CharField(max_length=100,default="")
    nombre = models.CharField(max_length=150, default="")
    capacidad = models.CharField(max_length=3, default="")
    disponible = models.BooleanField(default=True)