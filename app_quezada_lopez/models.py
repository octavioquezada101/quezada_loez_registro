from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre_produ=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=40)
    valor=models.IntegerField()
    foto=models.ImageField(upload_to='', null=True)


