from django.urls import path
from . views import index
from . views import nosotros
from . views import servicios
from . views import contacto
from . views import ubicacion
from . views import venta
from . views import register
from . views import home
from . views import agregar
from . views import agregarrec
from . views import eliminar
from . views import actualizar
from . views import actualizarrec
from . views import mantenedor
from app_quezada_lopez import views

urlpatterns = [
    path('', index, name='index' ),
    path('nosotros.html', nosotros, name='nosotros' ),
    path('servicios.html', servicios, name='servicios' ),
    path('contacto.html', contacto, name='contacto' ),
    path('ubicacion.html', ubicacion, name='ubicacion' ),   
    path('venta.html', venta, name='venta' ),
    path('mantenedor.html', mantenedor, name='mantenedor' ),
    path('home.html', home, name='home'),
    path('agregar/', agregar,name='agregar'),
    path('agregarrec/',agregarrec, name='agregarrec'),
    path('eliminar/<int:id>/', eliminar,name='eliminar'),
    path('actualizar/<int:id>/',actualizar,name='actualizar'),
    path('actualizar/actualizarrec/<int:id>/',actualizarrec,name='actualizarrec'),
    path('register/', register, name='register'),



]