from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.alquiler.models import Registrador, Estado, Alquiler
from django.urls import reverse_lazy
from apps.alquiler.forms import RegistradorForm, EstadoForm, AlquilerForm
from apps.cliente.forms import ClienteForm
from apps.habitacion.forms import HabitacionForm

# Create your views here.

def index(request):
    return HttpResponse("Index de alquiler")

class RegistradorList(ListView):
    model = Registrador
    template_name = 'alquiler/registrador/registrador_list.html'

class RegistradorInsert(CreateView):
    model = Registrador
    template_name = 'alquiler/registrador/registrador_form.html'
    form_class = RegistradorForm
    success_url = reverse_lazy('registrador_listar')
    
class RegistradorEdit(UpdateView):
    model = Registrador
    template_name = 'alquiler/registrador/registrador_form.html'
    form_class = RegistradorForm
    success_url = reverse_lazy('registrador_listar')

class RegistradorDelete(DeleteView):
    model = Registrador
    template_name = 'alquiler/registrador/registrador_delete.html'
    success_url = reverse_lazy('registrador_listar')

class AlquilerList(ListView):
    model = Alquiler
    template_name = 'alquiler/alquiler_list.html'

class AlquilerInsert(CreateView):
    model = Alquiler
    template_name = 'alquiler/alquiler_form.html'
    form_class = AlquilerForm
    success_url = reverse_lazy('alquiler_listar')
    
class AlquilerUpdate(UpdateView):
    model = Alquiler
    template_name = 'alquiler/alquiler_form.html'
    form_class = AlquilerForm
    success_url = reverse_lazy('alquiler_listar')

class AlquilerDelete(DeleteView):
    model = Alquiler
    template_name = 'alquiler/alquiler_delete.html'
    success_url = reverse_lazy('alquiler_listar')