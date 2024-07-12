# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView, EditarFormulario, EliminarFormulario

urlpatterns = [
    path('', views.principal, name='principal'),
    path('quienes-somos/', views.quienes_somos, name='quienes-somos'),
    path('arreglo-frenos/', views.arreglo_frenos, name='arreglo-frenos'),
    path('arreglos-motor/', views.arreglos_motor, name='arreglos-motor'),
    path('contacto/', views.contacto, name='contacto'),
    path('arreglo-transmision/', views.arreglo_transmision, name='arreglo-transmision'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('lista_formularios/', views.ListaFormularios.as_view(), name='lista_formularios'),
    path('editar_formulario/<int:pk>/', EditarFormulario.as_view(), name='editar_formulario'),
    path('eliminar_formulario/<int:pk>/', EliminarFormulario.as_view(), name='eliminar_formulario'),
    path('formularios/cambiar-estado/<int:pk>/', views.cambiar_estado_formulario, name='cambiar_estado_formulario'),
]
