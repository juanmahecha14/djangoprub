from django.shortcuts import render, redirect
from .forms import ClienteForm, VideojuegoForm, VentaForm
from .models import Cliente, Videojuego, Venta

def menu_principal(request):
    return render(request, 'juegos/menu_principal.html')

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
    else:
        form = ClienteForm()
    return render(request, 'juegos/formulario.html', {'form': form, 'titulo': 'Registrar Cliente'})

def registrar_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
    else:
        form = VideojuegoForm()
    return render(request, 'juegos/formulario.html', {'form': form, 'titulo': 'Registrar Videojuego'})

def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
    else:
        form = VentaForm()
    return render(request, 'juegos/formulario.html', {'form': form, 'titulo': 'Registrar Venta'})

def registro_exitoso(request):
    return render(request, 'juegos/exito.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'juegos/lista_clientes.html', {'clientes': clientes})

def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'juegos/lista_videojuegos.html', {'videojuegos': videojuegos})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'juegos/lista_ventas.html', {'ventas': ventas})
