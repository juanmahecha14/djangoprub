from django.test import TestCase
from juegos.forms import ClienteForm, VideojuegoForm, VentaForm
from juegos.models import Cliente, Videojuego

class ClienteFormTest(TestCase):
    def test_formulario_valido(self):
        datos = {
            'nombre': 'Laura Gómez',
            'correo': 'laura@example.com',
            'telefono': '3104567890'
        }
        form = ClienteForm(data=datos)
        self.assertTrue(form.is_valid())

class VideojuegoFormTest(TestCase):
    def test_formulario_valido(self):
        datos = {
            'titulo': 'CyberQuest',
            'genero': 'Estrategia',
            'precio': 85000,
            'stock': 12
        }
        form = VideojuegoForm(data=datos)
        self.assertTrue(form.is_valid())

class VentaFormTest(TestCase):
    def setUp(self):
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

    def test_formulario_valido(self):
        datos = {
            'cliente': self.cliente.id,
            'videojuego': self.juego.id,
            'cantidad': 2
        }
        form = VentaForm(data=datos)
        self.assertTrue(form.is_valid())