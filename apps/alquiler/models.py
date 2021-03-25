from django.db import models
from apps.cliente.models import Cliente
from apps.habitacion.models import Habitacion
# Create your models here.

class Registrador (models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    documento = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    observacion = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Estado (models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Alquiler (models.Model):
    fechaHoraEntrada = models.DateTimeField(null = False ,blank = False, auto_now=False, auto_now_add=False )
    fechaHoraSalida = models.DateTimeField(null = False ,blank = False, auto_now=False, auto_now_add=False )
    costoTotal = models.IntegerField()
    obsevacion = models.TextField(max_length=100)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    registrador = models.ForeignKey(Registrador, on_delete=models.CASCADE)
    estado  = models.ForeignKey(Estado, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.__str__(Alquiler)