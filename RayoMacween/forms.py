from django import forms
from .models import Formulario
from django.forms import TextInput, NumberInput, Select, Textarea


class Formulario(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'
        labels = {
            "rut":"",
            "nombre":"",
            "appaterno":"",
            "apmaterno":"",
            "edad":"",
            "id_genero":"",
            "celular":"",
            "descripcion":""

        }
        widgets = {
            'rut': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Rut',
                'style':'margin-bottom : 20px;'
                }),
            'nombre': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nombre',
                'style':'margin-bottom : 20px;'
                
                }),
                
            'appaterno': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Apellido Paterno',
                'style':'margin-bottom : 20px;'
                }),
            'apmaterno': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Apellido Materno',
                'style':'margin-bottom : 20px;'
                }),
            'edad': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Edad',
                'style':'margin-bottom : 20px;'
                }),
            'id_genero': Select(attrs={
                'class': "form-select",
                'style':'margin-bottom : 20px;'
                }),
            'celular': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Celular',
                'style':'margin-bottom : 20px;'
                }),
            'descripcion': Textarea(attrs={
                'class': "form-control",
                'rows':"5",
                'placeholder': 'Describa el problema',
                'style':'margin-bottom : 20px;'
                })
        }