from django.shortcuts import render, get_object_or_404
from .carrito import Carrito
from RayoMacween.models import Producto
from django.http import JsonResponse

def carrito_resumen(request):
	return render(request, "carrito_resumen.html", {})

def carrito_add(request):
	
	carrito = Carrito(request)
	if request.POST.get('action') == 'post':
		producto_id = int(request.POST.get('producto_id'))
		#producto_qty = int(request.POST.get('product_qty'))

		producto = get_object_or_404(Producto, id=producto_id)

		carrito.add(producto=producto)

		#carrito_quantity = carrito.__len__()

		response = JsonResponse({'Nombre producto': producto.nombre})
		#messages.success(request, ("Producto añadido al carrito"))
		return response

def carrito_delete(request):
	pass
	'''cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		# Call delete Function in Cart
		cart.delete(product=product_id)

		response = JsonResponse({'product':product_id})
		#return redirect('cart_summary')
		messages.success(request, ("Item Deleted From Shopping Cart..."))
		return response'''


def carrito_update(request):
	pass
	'''cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		cart.update(product=product_id, quantity=product_qty)

		response = JsonResponse({'qty':product_qty})
		#return redirect('cart_summary')
		messages.success(request, ("Your Cart Has Been Updated..."))
		return response'''