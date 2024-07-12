from django import forms
from django.core.exceptions import ValidationError
from .models import Formulario
from django import forms

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        exclude = ['user', 'estado']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rut'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'appaterno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Paterno'}),
            'apmaterno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Materno'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
            'id_genero': forms.Select(attrs={'class': 'form-select'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describa el problema'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        edad = cleaned_data.get('edad')
        id_genero = cleaned_data.get('id_genero')
        celular = cleaned_data.get('celular')
        rut = cleaned_data.get('rut')
        nombre = cleaned_data.get('nombre')
        appaterno = cleaned_data.get('appaterno')
        apmaterno = cleaned_data.get('apmaterno')

        if id_genero == 4 or id_genero is None:
            raise ValidationError('Debe elegir su género.')

        if edad <= 0:
            raise ValidationError('La edad no puede ser 0 ni un número negativo.')

        if any(not data or data.strip() == '' for data in [rut, nombre, appaterno, apmaterno, celular]):
            raise ValidationError('ERROR: Ningún campo puede quedar vacío')

        return cleaned_data

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) > 50:
            raise ValidationError('El nombre no puede superar 50 caracteres')
        return nombre

    def clean_appaterno(self):
        appaterno = self.cleaned_data.get('appaterno')
        if len(appaterno) > 50:
            raise ValidationError('El apellido paterno no puede superar 50 caracteres')
        return appaterno

    def clean_apmaterno(self):
        apmaterno = self.cleaned_data.get('apmaterno')
        if len(apmaterno) > 50:
            raise ValidationError('El apellido materno no puede superar 50 caracteres')
        return apmaterno

    def clean_celular(self):
        celular = self.cleaned_data.get('celular')
        if len(str(celular)) != 9:
            raise ValidationError('El celular debe contener 9 dígitos')
        return celular
    
class EditarFormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['descripcion', 'celular']

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        return descripcion
    