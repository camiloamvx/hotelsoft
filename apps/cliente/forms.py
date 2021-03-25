from django import forms
from apps.cliente.models import Cliente, Nacionalidad

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'direccion',
            'documento',
            'telefono',
        ]

        labels = {
            'nombre':'Nombre',
            'direccion':'Dirección',
            'documento':'Documento',
            'telefono':'Telefono',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'documento':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
        }
    
class NacionalidadForm(forms.ModelForm):
    class Meta:
        model = Nacionalidad
        fields = [
            'pais',
            'nacionalidad',
        ]

        labels = {
            'pais':'Pais',
            'nacionalidad':'Nacionalidad',
        }

        widgets = {
            'pais':forms.TextInput(attrs={'class':'form-control'}),
            'nacionalidad':forms.TextInput(attrs={'class':'form-control'}),
        }


