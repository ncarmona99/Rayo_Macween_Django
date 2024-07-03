from django.urls import path
from . import views


urlpatterns = [
    path('', views.carrito_resumen, name="carrito_resumen"),
    path('add/', views.carrito_add, name="carrito_add"),
    path('delete/', views.carrito_delete, name="carrito_delete"),
    path('update/', views.carrito_update, name="carrito_update")
]