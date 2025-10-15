from django.test import TestCase, Client
from django.urls import reverse
from juegos.models import Cliente, Videojuego, Venta

class TemplateRenderTest(TestCase):
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
        Venta.objects.create(
            cliente=self.cliente,
            videojuego=self.juego,
            cantidad=2
        )

    def test_template_menu_principal(self):
        respuesta = self.client.get(reverse('menu_principal'))
        self.assertTemplateUsed(respuesta, 'juegos/menu_principal.html')

    def test_template_formulario_cliente(self):
        respuesta = self.client.get(reverse('registrar_cliente'))
        self.assertTemplateUsed(respuesta, 'juegos/formulario.html')
        self.assertIn('form', respuesta.context)
        self.assertEqual(respuesta.context['titulo'], 'Registrar Cliente')

    def test_template_lista_clientes(self):
        respuesta = self.client.get(reverse('lista_clientes'))
        self.assertTemplateUsed(respuesta, 'juegos/lista_clientes.html')
        self.assertIn('clientes', respuesta.context)

    def test_template_lista_videojuegos(self):
        respuesta = self.client.get(reverse('lista_videojuegos'))
        self.assertTemplateUsed(respuesta, 'juegos/lista_videojuegos.html')
        self.assertIn('videojuegos', respuesta.context)

    def test_template_lista_ventas(self):
        respuesta = self.client.get(reverse('lista_ventas'))
        self.assertTemplateUsed(respuesta, 'juegos/lista_ventas.html')
        self.assertIn('ventas', respuesta.context)

    def test_template_exito(self):
        respuesta = self.client.get(reverse('registro_exitoso'))
        self.assertTemplateUsed(respuesta, 'juegos/exito.html')