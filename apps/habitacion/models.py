from django.db import models

# Create your models here.

class TipoHabitacion (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Habitacion (models.Model):
    numero = models.CharField(null= False , blank = False ,max_length=5)
    estado = models.CharField(max_length=50)
    costo =  models.IntegerField(null= False , blank = False )
    descripcion = models.CharField(max_length=80)
    Tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero