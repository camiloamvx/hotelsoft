from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.cliente.models import Cliente, Nacionalidad
from django.urls import reverse_lazy
from apps.cliente.forms import ClienteForm, NacionalidadForm

# Create your views here.

def index(request):
    return HttpResponse("Index de cliente")

class ClienteList(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'

class ClienteInsert(CreateView):
    model = Cliente
    template_name = 'cliente/cliente_form.html'
    form_class = ClienteForm
    second_form_class = NacionalidadForm
    success_url = reverse_lazy('cliente_listar')

    def get_context_data(self, **kwargs):
        context = super(ClienteInsert, self).get_context_data()
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *arg, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            cliente = form.save(commit = False)
            cliente.fnacionalidad = form2.save()
            cliente.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form, form2 = form2))

class ClienteUpdate(UpdateView):
    model = Cliente
    second_model = Nacionalidad
    template_name = 'cliente/cliente_form.html'
    form_class = ClienteForm
    second_form_class = NacionalidadForm
    success_url = reverse_lazy('cliente_listar')

    def get_context_data(self, **kwargs):
        context = super(ClienteUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        cliente = self.model.objects.get(id = pk)
        nacionalidad = self.second_model.objects.get(id = cliente.fnacionalidad_id)
        if 'form' not in context:
            context ['form'] = self.form_class()
        if 'form2' not in context:
            context ['form2'] = self.second_form_class(instance = nacionalidad)
        context['id'] = pk
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_cliente = kwargs['pk']
        cliente = self.model.objects.get(id = id_cliente)
        nacionalidad = self.second_model.objects.get(id = cliente.fnacionalidad_id)
        form = self.form_class(request.POST, instance = cliente)
        form2 = self.second_form_class(request.POST, instance = nacionalidad)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_delete.html'
    form_class = ClienteForm
    second_form_class = NacionalidadForm
    success_url = reverse_lazy('cliente_listar')