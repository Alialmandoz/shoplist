from django.utils.datetime_safe import datetime
from django.db import models

# Create your models here.


class Post(models.Model):
    producto = models.TextField(null=True, blank=True, )
    precio = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.producto)


class Compra(models.Model):
    producto = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_compra = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.fecha_compra)


