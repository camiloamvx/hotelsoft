from django import forms
from django.db.models import fields
from django.forms import widgets
from apps.alquiler.models import Registrador, Estado, Alquiler

class RegistradorForm(forms.ModelForm):
    class Meta:
        model = Registrador
        fields = [
            'nombre',
            'direccion',
            'documento',
            'estado',
            'observacion',
        ]

        labels = {
            'nombre':'Nombre',
            'direccion':'Dirección',
            'documento':'Documento',
            'estado':'Estado',
            'observacion':'Observación',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'documento':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.TextInput(attrs={'class':'form-control'}),
            'observacion':forms.Textarea(attrs={'class':'form-control'}),
        }

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = [
            'nombre',
        ]

        labels = {
            'nombre':'Estado',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
        }

class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = [
            'fechaHoraEntrada',
            'fechaHoraSalida',
            'costoTotal',
            'obsevacion',
            'habitacion',
            'cliente',
            'registrador',
            'estado',
        ]

        labels = {
            'fechaHoraEntrada':'Fecha hora entrada',
            'fechaHoraSalida':'Fecha hora salida',
            'costoTotal':'Costo Total',
            'obsevacion':'Observación',
            'habitacion':'Habitación',
            'cliente':'Cliente',
            'registrador':'Registrador',
            'estado':'Estado', 
        }

        widgets = {
            'fechaHoraEntrada':forms.TextInput(attrs={'class':'form-control'}),
            'fechaHoraSalida':forms.TextInput(attrs={'class':'form-control'}),
            'costoTotal':forms.TextInput(attrs={'class':'form-control'}),
            'obsevacion':forms.Textarea(attrs={'class':'form-control'}),
            'habitacion':forms.Select(attrs={'class':'form-control'}),
            'cliente':forms.Select(attrs={'class':'form-control'}),
            'registrador':forms.Select(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control'}),
        }

