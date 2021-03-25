from django.db import models

# Create your models here.

class Nacionalidad (models.Model): 
    pais = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.Nacionalidad

class Cliente (models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    documento = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fnacionalidad = models.ForeignKey(Nacionalidad, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre