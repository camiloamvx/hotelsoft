from django.conf.urls import url, include
from apps.habitacion.views import index, TipoHabitacionList, TipoHabitacionInsert, TipoHabitacionUpdate, TipoHabitacionDelete, HabitacionList, HabitacionCreate, HabitacionUpdate, HabitacionDelete, ReporteHabitacionPdf, ReporteHabitacionExcel

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^tipo/listar$', TipoHabitacionList.as_view(), name="tipo_listar" ),
    url(r'^tipo/nuevo$', TipoHabitacionInsert.as_view(), name="tipo_insertar" ),
    url(r'^tipo/editar/(?P<pk>\d+)$', TipoHabitacionUpdate.as_view(), name="tipo_editar"),
    url(r'^tipo/eliminar/(?P<pk>\d+)$', TipoHabitacionDelete.as_view(), name="tipo_eliminar"),
    url(r'^listar$', HabitacionList.as_view(), name="habitacion_listar"),
    url(r'^nuevo$', HabitacionCreate.as_view(), name="habitacion_insertar"),
    url(r'^editar/(?P<pk>\d+)$', HabitacionUpdate.as_view(), name="habitacion_editar"),
    url(r'^eliminar/(?P<pk>\d+)$', HabitacionDelete.as_view(), name="habitacion_eliminar"),
    url(r'^reporte_habitacion_pdf/$', ReporteHabitacionPdf.as_view(), name="reporte_habitacion_pdf"),
    url(r'^reporte_habitacion_excel/$', ReporteHabitacionExcel.as_view(), name="reporte_habitacion_excel"),
]
    