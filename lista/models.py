from django.utils.datetime_safe import datetime
from django.db import models

# Create your models here.


class Compra(models.Model):
    fecha_compra = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.pk) + ": " + str(self.fecha_compra)


class Producto(models.Model):
    descripcion = models.CharField(max_length=200, null=True, blank=True,)
    marca = models.CharField(max_length=200, null=True, blank=True,)
    precio = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.descripcion + " " + self.marca)


class Post(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.producto)


