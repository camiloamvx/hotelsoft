from django import forms
from apps.habitacion.models import Habitacion, TipoHabitacion

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = [
            'numero',
            'estado',
            'costo',
            'descripcion',
            'Tipo',
        ]

        labels = {
            'numero':'Numero',
            'estado':'Estado',
            'costo':'Costo',
            'descripcion':'Descripción',
            'Tipo':'Tipo',
        }

        widgets = {
            'numero':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.TextInput(attrs={'class':'form-control'}),
            'costo':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
            'Tipo':forms.Select(attrs={'class':'form-control'}),
        }

class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = TipoHabitacion
        fields = [
            'nombre',
            'descripcion',
        ]

        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripcion',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
        }