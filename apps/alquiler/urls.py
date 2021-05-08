from apps.cliente.views import ClienteList
from django.conf.urls import url, include
from apps.alquiler.views import RegistradorDelete, index, RegistradorList, RegistradorInsert, RegistradorEdit, AlquilerList, AlquilerInsert, AlquilerUpdate, AlquilerDelete, ReporteAlquilerPdf, ReporteAlquilerExcel, EstadoList, EstadoInsert, EstadoUpdate, EstadoDelete

urlpatterns = [
    url(r'^$', index),
    url(r'^registrador/listar$', RegistradorList.as_view(), name='registrador_listar'),
    url(r'^registrador/nuevo$', RegistradorInsert.as_view(), name='registrador_nuevo'),
    url(r'^registrador/editar/(?P<pk>\d+)$', RegistradorEdit.as_view(), name="registrador_editar"),
    url(r'^registrador/eliminar/(?P<pk>\d+)$', RegistradorDelete.as_view(), name="registrador_eliminar"),
    url(r'^estado/listar$', EstadoList.as_view(), name='estado_listar'),
    url(r'^estado/nuevo$', EstadoInsert.as_view(), name='estado_insertar'),
    url(r'^estado/editar/(?P<pk>\d+)$', EstadoUpdate.as_view(), name="estado_editar"),
    url(r'^estado/eliminar/(?P<pk>\d+)$', EstadoDelete.as_view(), name="estado_eliminar"),
    url(r'^listar$', AlquilerList.as_view(), name='alquiler_listar'),
    url(r'^nuevo$', AlquilerInsert.as_view(), name='alquiler_insertar'),
    url(r'^editar/(?P<pk>\d+)$', AlquilerUpdate.as_view(), name="alquiler_editar"),
    url(r'^eliminar/(?P<pk>\d+)$', AlquilerDelete.as_view(), name="alquiler_eliminar"),
    url(r'^reporte_alquiler_pdf/$', ReporteAlquilerPdf.as_view(), name="reporte_alquiler_pdf"),
    url(r'^reporte_alquiler_excel/$', ReporteAlquilerExcel.as_view(), name="reporte_alquiler_excel"),
]
