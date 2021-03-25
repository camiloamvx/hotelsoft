from django.test.client import Client
from apps.cliente.models import Cliente
from django.test import TestCase
from apps.alquiler.models import Alquiler, Registrador, Estado

class RegistradorTestCase(TestCase):
    def setUp(self):
        Registrador.objects.create(nombre = 'Juan', documento = '120320200', direccion = 'cr30 #30-30', estado = 'Bogota')
        
    def test_registrador_tiene_documento(self):
        """Los registradores pueden tener documentos exitosamente"""
        Juan = Registrador.objects.get(documento = '1234567')
        self.assertContains(Juan.documento, '1234567')
        
        
