from os import name
from django.conf.urls import url, include
from apps.usuarios.views import RegistroUsuario

urlpatterns = [
    url(r'^nuevo$', RegistroUsuario.as_view(), name="registrar"),
]
