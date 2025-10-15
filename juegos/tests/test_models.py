from django.test import TestCase
from juegos.models import Cliente, Videojuego, Venta

class ClienteModelTest(TestCase):
    def test_creacion_cliente(self):
        cliente = Cliente.objects.create(
            nombre="Ana Torres",
            correo="ana@example.com",
            telefono="3001234567"
        )
        self.assertEqual(cliente.nombre, "Ana Torres")
        self.assertEqual(cliente.correo, "ana@example.com")
        self.assertEqual(cliente.telefono, "3001234567")
        self.assertEqual(str(cliente), "Ana Torres")

class VideojuegoModelTest(TestCase):
    def test_creacion_videojuego(self):
        juego = Videojuego.objects.create(
            titulo="Sphere",
            genero="Aventura",
            precio=75000,
            stock=10
        )
        self.assertEqual(juego.titulo, "Sphere")
        self.assertEqual(juego.genero, "Aventura")
        self.assertEqual(juego.precio, 75000)
        self.assertEqual(juego.stock, 10)
        self.assertEqual(str(juego), "Sphere")

class VentaModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Carlos Ruiz",
            correo="carlos@example.com",
            telefono="3109876543"
        )
        self.juego = Videojuego.objects.create(
            titulo="Sphere",
            genero="Aventura",
            precio=50000,
            stock=5
        )

    def test_creacion_venta_y_total(self):
        venta = Venta.objects.create(
            cliente=self.cliente,
            videojuego=self.juego,
            cantidad=2
        )
        self.assertEqual(venta.cantidad, 2)
        self.assertEqual(venta.total, 100000)
        self.assertEqual(str(venta), "Venta de Sphere a Carlos Ruiz")