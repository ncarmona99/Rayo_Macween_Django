from django.shortcuts import render, get_object_or_404
from .carrito import Carrito
from RayoMacween.models import Producto
from django.http import JsonResponse


def carrito_resumen(request):
    carrito = Carrito(request)
    carrito_productos = carrito.obtener_productos()
    return render(request, "carrito_resumen.html", {"carrito_productos": carrito_productos})

def carrito_add(request):
    carrito = Carrito(request)
    producto_id = int(request.POST.get('producto_id'))
    producto = get_object_or_404(Producto, id=producto_id)
    cantidad = int(request.POST.get('cantidad', 1))
    carrito.add(producto=producto, cantidad=cantidad)
    return JsonResponse({'total_cantidad': carrito.__len__()})

def carrito_update(request):
    carrito = Carrito(request)
    producto_id = int(request.POST.get('producto_id'))
    cantidad = int(request.POST.get('cantidad'))
    producto = get_object_or_404(Producto, id=producto_id)
    if cantidad > 0:
        carrito.update(producto=producto, cantidad=cantidad)
    else:
        carrito.delete(producto=producto)
    return JsonResponse({'total_cantidad': carrito.__len__(), 'total_price': carrito.obtener_precio_total()})

def carrito_delete(request):
    carrito = Carrito(request)
    producto_id = int(request.POST.get('producto_id'))
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.delete(producto=producto)
    return JsonResponse({'total_cantidad': carrito.__len__(), 'total_price': carrito.obtener_precio_total()})
