from django.test import TestCase
from apps.habitacion.models import Habitacion, TipoHabitacion

class HabitacionTestCase(TestCase):
    def setUp(self):
        Habitacion.objects.create()
