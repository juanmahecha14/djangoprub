from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_principal, name='menu_principal'),
    path('registrar-cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('registrar-videojuego/', views.registrar_videojuego, name='registrar_videojuego'),
    path('registrar-venta/', views.registrar_venta, name='registrar_venta'),
    path('exito/', views.registro_exitoso, name='registro_exitoso'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('videojuegos/', views.lista_videojuegos, name='lista_videojuegos'),
    path('ventas/', views.lista_ventas, name='lista_ventas'),
]
