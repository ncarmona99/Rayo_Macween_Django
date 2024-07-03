from django.shortcuts import render,redirect
from .forms import Formulario
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
    return render(request,'RayoMacween/arreglo-transmision.html',context)