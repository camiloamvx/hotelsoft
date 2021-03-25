from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.habitacion.models import Habitacion, TipoHabitacion
from django.urls import reverse_lazy
from apps.habitacion.forms import HabitacionForm, TipoHabitacionForm
# Create your views here.

def index(request):
    return HttpResponse("Index de habitacion")

class TipoHabitacionList(ListView):
    model = TipoHabitacion
    template_name = 'habitacion/tipo/tipo_list.html'

class TipoHabitacionInsert(CreateView):
    model = TipoHabitacion
    template_name = 'habitacion/tipo/tipo_form.html'
    form_class = TipoHabitacionForm
    success_url = reverse_lazy('tipo_listar')

class TipoHabitacionUpdate(UpdateView):
    model = TipoHabitacion
    template_name = 'habitacion/tipo/tipo_form.html'
    form_class = TipoHabitacionForm
    success_url = reverse_lazy('tipo_listar')

class TipoHabitacionDelete(DeleteView):
    model = TipoHabitacion
    template_name = 'habitacion/tipo/tipo_delete.html'
    success_url = reverse_lazy('tipo_listar')

class HabitacionList(ListView):
    model = Habitacion
    template_name = 'habitacion/habitacion_list.html'
    
class HabitacionCreate(CreateView):
    model = Habitacion
    template_name = 'habitacion/habitacion_form.html'
    form_class = HabitacionForm
    success_url = reverse_lazy('habitacion_listar')

class HabitacionUpdate(UpdateView):
    model = Habitacion
    template_name = 'habitacion/habitacion_form.html'
    form_class = HabitacionForm
    success_url = reverse_lazy('habitacion_listar')

class HabitacionDelete(DeleteView):
    model = Habitacion
    template_name = 'habitacion/habitacion_delete.html'
    success_url = reverse_lazy('habitacion_listar')
    



