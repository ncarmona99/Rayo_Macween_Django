from RayoMacween.models import Producto

class Carrito():
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get('session_key')
        if 'session_key' not in self.session:
            carrito = self.session['session_key'] = {}
        self.carrito = carrito

    def add(self, producto, cantidad=1):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            self.carrito[producto_id]['cantidad'] += cantidad
        else:
            self.carrito[producto_id] = {'precio': str(producto.precio), 'cantidad': cantidad}
        self.session.modified = True

    def update(self, producto, cantidad):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            if cantidad > 0:
                self.carrito[producto_id]['cantidad'] = cantidad
            else:
                self.delete(producto)
        self.session.modified = True

    def delete(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
        self.session.modified = True

    def obtener_productos(self):
        productos_ids = self.carrito.keys()
        productos = Producto.objects.filter(id__in=productos_ids)
        return productos

    def __len__(self):
        return sum(item['cantidad'] for item in self.carrito.values())

    def obtener_precio_total(self):
        total = 0
        for item in self.carrito.values():
            total += int(item['precio']) * item['cantidad']
        return total
