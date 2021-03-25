from django.contrib import admin
from apps.cliente.models import Cliente, Nacionalidad
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Nacionalidad)