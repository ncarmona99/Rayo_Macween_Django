from django.shortcuts import render

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
    context={}
    return render(request,'RayoMacween/contacto.html',context)

def arreglos_motor(request):
    context={}
    return render(request,'RayoMacween/arreglos-motor.html',context)

def arreglo_transmision(request):
    context={}
    return render(request,'RayoMacween/arreglo-transmision.html',context)

