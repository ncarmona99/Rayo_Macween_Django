<<<<<<< HEAD
from django.shortcuts import render,redirect
from .forms import Formulario
=======
from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

>>>>>>> origin/Bicho
# Create your views here.


def principal(request):
    context={}
    return render(request,'RayoMacween/principal.html',context)

def quienes_somos(request):
    context={}
    return render(request,'RayoMacween/quienes-somos.html',context)

def arreglo_frenos(request):
    context={}
    return render(request,'RayoMacween/arreglo-frenos.html',context)

def contacto(request):
    data = {
        'form': Formulario()
    }
    if request.method == 'POST':
        formulario = Formulario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
            return redirect('contacto')
        else:
            data['form'] = formulario
            formulario = Formulario()
    return render(request,'RayoMacween/contacto.html',data)
        
def arreglos_motor(request):
    context={}
    return render(request,'RayoMacween/arreglos-motor.html',context)

def arreglo_transmision(request):
    context={}
<<<<<<< HEAD
    return render(request,'RayoMacween/arreglo-transmision.html',context)
=======
    return render(request,'RayoMacween/arreglo-transmision.html',context)

def tienda(request):
    productos = Producto.objects.all()
    return render(request,'RayoMacween/tienda.html',{'productos':productos})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión exitosamente.")
            return redirect('principal')
        else:
            messages.success(request, "Hubo un error, por favor inténtalo nuevamente.")
            return redirect('login')
    else:
        return render(request,'RayoMacween/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("Ha salido de la sesión."))
    return redirect('principal')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Te has registrado éxitosamente."))
            return redirect('principal')
        else:
            messages.success(request, ("Hubo un problema. Por favor intenta de nuevo."))
            return redirect('register')
    else:
        return render(request,'RayoMacween/registrarse.html', {'form': form})

def categoria(request, foo):
    print(f"Buscando la categoría: {foo}")
    try:
        categoria = Categoria.objects.get(nombre=foo)
        productos = Producto.objects.filter(categoria=categoria)
        return render(request, 'RayoMacween/categoria.html', {'productos':productos, 'categoria':categoria})
    except:
        messages.success(request, ("No existe esa categoría."))
        return redirect('principal')
>>>>>>> origin/Bicho
