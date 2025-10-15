from django.test import SimpleTestCase
from django.urls import reverse, resolve
from juegos.views import (
    menu_principal,
    registrar_cliente,
    registrar_videojuego,
    registrar_venta,
    registro_exitoso,
    lista_clientes,
    lista_videojuegos,
    lista_ventas
)

class UrlsTest(SimpleTestCase):
    def test_url_menu_principal(self):
        url = reverse('menu_principal')
        self.assertEqual(resolve(url).func, menu_principal)

    def test_url_registrar_cliente(self):
        url = reverse('registrar_cliente')
        self.assertEqual(resolve(url).func, registrar_cliente)

    def test_url_registrar_videojuego(self):
        url = reverse('registrar_videojuego')
        self.assertEqual(resolve(url).func, registrar_videojuego)

    def test_url_registrar_venta(self):
        url = reverse('registrar_venta')
        self.assertEqual(resolve(url).func, registrar_venta)

    def test_url_registro_exitoso(self):
        url = reverse('registro_exitoso')
        self.assertEqual(resolve(url).func, registro_exitoso)

    def test_url_lista_clientes(self):
        url = reverse('lista_clientes')
        self.assertEqual(resolve(url).func, lista_clientes)

    def test_url_lista_videojuegos(self):
        url = reverse('lista_videojuegos')
        self.assertEqual(resolve(url).func, lista_videojuegos)

    def test_url_lista_ventas(self):
        url = reverse('lista_ventas')
        self.assertEqual(resolve(url).func, lista_ventas)