from django.contrib import admin
from .models import Productos
from django.contrib.auth.models import Group

# Register your models here.
class productoAdmin(admin.ModelAdmin):
    list_display="nombre_produ","descripcion","valor","foto"

admin.site.register(Productos,productoAdmin)

# Define los grupos y los permisos correspondientes
class CustomAdminGroup(Group):
    class Meta:
        proxy = True

# Registra el grupo personalizado en el panel de administración
admin.site.register(CustomAdminGroup)

# Asigna los permisos al grupo personalizado


