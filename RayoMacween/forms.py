from django import forms
from .models import Formulario
from django.forms import TextInput, NumberInput, Select, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo electrónico'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
		self.fields['username'].label = ''
		self.fields['username'].help_text = ''

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = ''

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = ''