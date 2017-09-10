from django.utils.datetime_safe import datetime
from django.db import models

# Create your models here.


class Compra(models.Model):
    fecha_compra = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.fecha_compra)


class Post(models.Model):
    producto = models.TextField(null=True, blank=True, )
    precio = models.IntegerField(null=True, blank=True)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.producto)

    
class Producto(models.Model):
    producto = ""
    marca = ""
    precio = ""