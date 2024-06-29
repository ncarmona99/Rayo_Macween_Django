from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('quienes-somos/', views.quienes_somos, name='quienes-somos'),
    path('arreglo-frenos/', views.arreglo_frenos, name='arreglo-frenos'),
    path('arreglos-motor/', views.arreglos_motor, name='arreglos-motor'),
    path('contacto/', views.contacto, name='contacto'),
    path('arreglo-transmision/', views.arreglo_transmision, name='arreglo-transmision'),
    path('tienda/', views.tienda, name='tienda'),
]