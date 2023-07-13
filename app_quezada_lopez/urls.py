from django.urls import path
from .views import index, nosotros, pagar, boleta, vacio, servicios, contacto, ubicacion, register, home, agregar, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, agregarrec, eliminar, actualizar, actualizarrec, mantenedor
from . views import carrito

urlpatterns = [
    path('', index, name='index'),
    path('nosotros.html', nosotros, name='nosotros'),
    path('vacio.html', vacio, name='vacio'),
    path('pagar.html', pagar, name='pagar'),
    path('boleta.html', boleta, name='boleta'),
    path('servicios.html', servicios, name='servicios'),
    path('contacto.html', contacto, name='contacto'),
    path('ubicacion.html', ubicacion, name='ubicacion'),
    path('mantenedor.html', mantenedor, name='mantenedor'),
    path('home.html', home, name='home'),
    path('agregar/', agregar, name='agregar'),
    path('agregarrec/', agregarrec, name='agregarrec'),
    path('eliminar/<int:id>/', eliminar, name='eliminar'),
    path('actualizar/<int:id>/', actualizar, name='actualizar'),
    path('actualizarrec/<int:id>/', actualizarrec, name='actualizarrec'),
    path('register/', register, name='register'),
#carrito
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name='Sub'),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('carrito.html', carrito , name="carrito" ),
]
