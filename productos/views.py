from django.shortcuts import render,redirect
from .models import Producto

productos = []

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def agregar_producto(request):
    
    nombre = request.POST['textoProducto']
    precio = request.POST['textoPrecio']
    unidad = request.POST['textoUnidad']

       
    precio = precio.replace(',', '.')

    try:
        precio = float(precio)
        precio = f"{precio:.2f}"
    except ValueError:
        productos = Producto.objects.all()
        return render(request, 'listar.html', {'productos': productos,'error': 'El precio debe ser un número decimal.'})

    Producto.objects.create(
        nombre=nombre, precio=precio, cantidad=unidad
    )
    return redirect('/')


def editar_producto(request,id):
    id = request.POST['id']
    nombre = request.POST['textoProducto']
    precio = request.POST['textoPrecio']
    unidad = request.POST['textoUnidad']
    
    precio = precio.replace(',', '.')
    
    try:
        precio = float(precio)
        precio = f"{precio:.2f}"
    except ValueError:
        productos = Producto.objects.all()
        return render(request, 'listar.html', {'productos': productos, 'errorEditar': 'El precio debe ser un número decimal.'})

    producto = Producto.objects.get(id=id)
    producto.nombre = nombre
    producto.precio = precio
    producto.cantidad = unidad
    producto.save()

    return redirect('/')



def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/')
