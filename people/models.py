from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    edad = models.CharField(max_length=5)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre
