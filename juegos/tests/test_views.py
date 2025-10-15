from django.test import TestCase, Client
from django.urls import reverse
from juegos.models import Cliente, Videojuego, Venta

class VistasTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cliente = Cliente.objects.create(
            nombre='Carlos Ruiz',
            correo='carlos@example.com',
            telefono='3109876543'
        )
        self.juego = Videojuego.objects.create(
            titulo='Sphere',
            genero='Aventura',
            precio=50000,
            stock=5
        )

    def test_menu_principal(self):
        respuesta = self.client.get(reverse('menu_principal'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, 'juegos/menu_principal.html')

    def test_registro_exitoso(self):
        respuesta = self.client.get(reverse('registro_exitoso'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, 'juegos/exito.html')

    def test_lista_clientes(self):
        respuesta = self.client.get(reverse('lista_clientes'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Carlos Ruiz')

    def test_lista_videojuegos(self):
        respuesta = self.client.get(reverse('lista_videojuegos'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Sphere')

    def test_registrar_cliente_post(self):
        datos = {
            'nombre': 'Laura Gómez',
            'correo': 'laura@example.com',
            'telefono': '3104567890'
        }
        respuesta = self.client.post(reverse('registrar_cliente'), data=datos)
        self.assertEqual(respuesta.status_code, 302)  # redirección

    def test_registrar_videojuego_post(self):
        datos = {
            'titulo': 'CyberQuest',
            'genero': 'Estrategia',
            'precio': 85000,
            'stock': 12
        }
        respuesta = self.client.post(reverse('registrar_videojuego'), data=datos)
        self.assertEqual(respuesta.status_code, 302)

    def test_registrar_venta_post(self):
        datos = {
            'cliente': self.cliente.id,
            'videojuego': self.juego.id,
            'cantidad': 2
        }
        respuesta = self.client.post(reverse('registrar_venta'), data=datos)
        self.assertEqual(respuesta.status_code, 302)