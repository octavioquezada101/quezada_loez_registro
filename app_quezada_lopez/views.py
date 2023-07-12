import os
import re
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForm
from app_quezada_lopez.models import Productos
from .carrito import Carrito

def carrito(request):
    productos = Productos.objects.all()
    return render(request, 'app_quezada_lopez/carrito.html', {'productos':productos})


def home(request):
    return render(request, 'app_quezada_lopez/home.html')

def pagar(request):
    return render(request, 'app_quezada_lopez/pagar.html')

def index(request):
    return render(request, 'app_quezada_lopez/index.html')

def servicios(request):
    return render(request, 'app_quezada_lopez/servicios.html')

def nosotros(request):
    return render(request, 'app_quezada_lopez/nosotros.html')

def contacto(request):
    return render(request, 'app_quezada_lopez/contacto.html')

def ubicacion(request):
    return render(request, 'app_quezada_lopez/ubicacion.html')

#def comprar(request, id):
#    return render(request, 'app_quezada_lopez/comprar.html')



def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    pro = Productos.objects.get(id=producto_id)
    carrito.agregar_carrito(pro)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    pro = Productos.objects.get(id=producto_id)
    carrito.eliminar(pro)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    pro = Productos.objects.get(id=producto_id)
    carrito.restar(pro)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

@login_required
def venta(request):
    if request.user.is_superuser: 
        return redirect('mantenedor')  
    else:        
        return render(request, 'app_quezada_lopez/venta.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def mantenedor(request):
    pro = Productos.objects.all()
    return render(request, 'app_quezada_lopez/mantenedor.html', {'pro': pro})

def agregar(request):
    return render(request, 'app_quezada_lopez/agregar.html')

#def agregarrec(request):
#    x = request.POST['nombre_produ']
#    y = request.POST['descripcion']
#    z = request.POST['valor']
#    f = request.FILES.get('foto')
#    pro = Productos(nombre_produ=x, descripcion=y, valor=z, foto=f)
#    pro.save()
#    return redirect('mantenedor')


def agregarrec(request):
    x = request.POST['nombre_produ']
    y = request.POST['descripcion']
    z = request.POST['valor']
    f = request.FILES.get('foto')

    if not z.isdigit():
        messages.add_message(request, messages.ERROR, 'Ingreso incorrecto en el campo valor. Vuelva a ingresar.')
        return redirect('agregar')

    pro = Productos(nombre_produ=x, descripcion=y, valor=z, foto=f)
    pro.save()
    return redirect('mantenedor')


def eliminar(request, id):
    pro = Productos.objects.get(id=id)
    if pro.foto:
        foto_path = pro.foto.path
        if os.path.exists(foto_path):
            os.remove(foto_path)       
    pro.delete()
    return redirect('mantenedor')

def actualizar(request, id):
    pro = Productos.objects.get(id=id)
    return render(request, 'app_quezada_lopez/actualizar.html', {'pro': pro})

def actualizarrec(request, id):
    pro = Productos.objects.get(id=id)
    if request.method == 'POST':
        x = request.POST['nombre_produ']
        y = request.POST['descripcion']
        z = request.POST['valor']
        f = request.FILES.get('foto')
        
        if not z.isdigit():
            messages.add_message(request, messages.ERROR, 'Ingreso incorrecto en el campo valor. Vuelva a ingresar.')
            return render(request, 'app_quezada_lopez/actualizar.html', {'pro': pro})

        pro.nombre_produ = x
        pro.descripcion = y
        pro.valor = z
        if f:
            pro.foto = f    
        pro.save()
        return redirect('mantenedor')
    return render(request, 'app_quezada_lopez/actualizar.html', {'pro': pro})


