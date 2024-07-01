from RayoMacween.models import Producto

class Carrito():
    def __init__(self, request):
        self.session = request.session
        self.request = request
        carrito = self.session.get('session_key')

        if 'session_key' not in request.session:
            carrito = self.session['session_key'] = {}

        self.carrito = carrito

    def add(self, producto):
        producto_id = str(producto.id)

        if producto_id in self.carrito:
            pass
        else:
            self.carrito[producto_id] = {'precio': str(producto.precio)}
    
        self.session.modified = True
