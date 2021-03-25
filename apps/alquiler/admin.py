from django.contrib import admin
from apps.alquiler.models import Alquiler, Registrador, Estado
# Register your models here.

admin.site.register(Alquiler)
admin.site.register(Registrador)
admin.site.register(Estado)

