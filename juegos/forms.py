from django import forms
from .models import Cliente, Videojuego, Venta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = '__all__'

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'videojuego', 'cantidad']  # total se calcula automáticamente
