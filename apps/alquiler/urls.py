from apps.cliente.views import ClienteList
from django.conf.urls import url, include
from apps.alquiler.views import RegistradorDelete, index, RegistradorList, RegistradorInsert, RegistradorEdit, AlquilerList, AlquilerInsert, AlquilerUpdate, AlquilerDelete, ReporteAlquilerPdf, ReporteAlquilerExcel

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^registrador/listar$', RegistradorList.as_view(), name='registrador_listar'),
    url(r'^registrador/nuevo$', RegistradorInsert.as_view(), name='registrador_nuevo'),
    url(r'^registrador/editar/(?P<pk>\d+)$', RegistradorEdit.as_view(), name="registrador_editar"),
    url(r'^registrador/eliminar/(?P<pk>\d+)$', RegistradorDelete.as_view(), name="registrador_eliminar"),
    url(r'^listar$', AlquilerList.as_view(), name='alquiler_listar'),
    url(r'^nuevo$', AlquilerInsert.as_view(), name='alquiler_insertar'),
    url(r'^editar/(?P<pk>\d+)$', AlquilerUpdate.as_view(), name="alquiler_editar"),
    url(r'^eliminar/(?P<pk>\d+)$', AlquilerDelete.as_view(), name="alquiler_eliminar"),
    url(r'^reporte_alquiler_pdf/$', ReporteAlquilerPdf.as_view(), name="reporte_alquiler_pdf"),
    url(r'^reporte_alquiler_excel/$', ReporteAlquilerExcel.as_view(), name="reporte_alquiler_excel"),
]
