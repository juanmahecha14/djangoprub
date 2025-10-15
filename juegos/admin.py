from django.contrib import admin
from .models import Cliente, Videojuego, Venta

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono')
    search_fields = ('nombre', 'correo')

@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'precio', 'stock')
    list_filter = ('genero',)
    search_fields = ('titulo',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'videojuego', 'cantidad', 'total', 'fecha')
    list_filter = ('fecha',)
    autocomplete_fields = ('cliente', 'videojuego')
