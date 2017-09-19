from django.forms import ModelForm
from lista.models import *


class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = ('fecha_compra',)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('producto',)


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'marca', 'precio',)