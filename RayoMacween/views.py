from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormularioForm 
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .models import Formulario
from .forms import EditarFormularioForm
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView


def principal(request):
    context={}
    return render(request,'RayoMacween/principal.html',context)

def quienes_somos(request):
    context={}
    return render(request,'RayoMacween/quienes-somos.html',context)

def arreglo_frenos(request):
    context={}
    return render(request,'RayoMacween/arreglo-frenos.html',context)

def arreglos_motor(request):
    context={}
    return render(request,'RayoMacween/arreglos-motor.html',context)

def arreglo_transmision(request):
    context={}
    return render(request,'RayoMacween/arreglo-transmision.html',context)

def registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('principal')  
    else:
        form = UserCreationForm()
    return render(request, 'RayoMacween/registrarse.html', {'form': form})

@login_required  
def contacto(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.user = request.user 
            formulario.save()  
            messages.success(request, 'Formulario enviado con éxito.')
            return redirect('contacto')  
        else:
            messages.error(request, 'Ha habido un error al enviar el formulario.')  
    else:
        form = FormularioForm()

    return render(request, 'RayoMacween/contacto.html', {'form': form})

class CustomLoginView(LoginView):
    
    template_name = 'RayoMacween/login.html'

    def get(self, request, *args, **kwargs):
        next_url = request.GET.get('next', '')
        if 'contacto' in next_url:
            messages.info(request, 'Por favor inicie sesión para entrar a contacto.')
        return super().get(request, *args, **kwargs)

    
class ListaFormularios(LoginRequiredMixin, ListView):
    model = Formulario
    template_name = 'RayoMacween/lista_formularios.html'
    context_object_name = 'formularios'
    
    def get_queryset(self):
        if self.request.user.is_superuser: 
            return Formulario.objects.all()
        else:  
            return Formulario.objects.filter(user=self.request.user)
        
class EditarFormulario(UpdateView):
    model = Formulario
    form_class = EditarFormularioForm
    template_name = 'RayoMacween/editar_formulario.html'
    success_url = reverse_lazy('lista_formularios')

    def get_queryset(self):
        if self.request.user.is_superuser: 
            return Formulario.objects.all()
        else: 
            return Formulario.objects.filter(user=self.request.user)
    
class EliminarFormulario(DeleteView):
    model = Formulario
    template_name = 'RayoMacween/eliminar_formulario.html'
    success_url = reverse_lazy('lista_formularios')   

@login_required
def cambiar_estado_formulario(request, pk):
    if request.method == 'POST' and request.user.is_superuser:
        formulario = get_object_or_404(Formulario, pk=pk)
        nuevo_estado = request.POST.get('estado')
        formulario.estado = nuevo_estado
        formulario.save()
        return redirect('lista_formularios')
    return redirect('lista_formularios')    