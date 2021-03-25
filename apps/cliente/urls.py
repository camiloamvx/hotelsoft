from django.conf.urls import url, include
from apps.cliente.views import index, ClienteList, ClienteInsert, ClienteUpdate, ClienteDelete


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^listar$', ClienteList.as_view(), name="cliente_listar" ),
    url(r'^nuevo$', ClienteInsert.as_view(), name="cliente_insertar" ),
    url(r'^editar/(?P<pk>\d+)$', ClienteUpdate.as_view(), name="cliente_editar"),
    url(r'^eliminar/(?P<pk>\d+)$', ClienteDelete.as_view(), name="cliente_eliminar"),
]