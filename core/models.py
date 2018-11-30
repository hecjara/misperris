from django.db import models
from datetime import datetime

# Create your models here.

class Raza(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=6)

    def __str__(self):
        return self.nombre


class PerroFundacion(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Género")
    fechaIngreso = models.DateField(verbose_name="Fecha Ingreso")
    fechaNacimiento = models.DateField(verbose_name="Fecha Nacimiento")
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True)    

    def __str__(self):
        return self.nombre

    def fecha_nacimiento(self):
        return self.fechaNacimiento.strftime('%Y-%m-%d')

    def fecha_ingreso(self):
        return self.fechaIngreso.strftime('%Y-%m-%d')





    class Meta:
        verbose_name = "Perro Fundacion"
        verbose_name_plural = "Perros Fundacion"

