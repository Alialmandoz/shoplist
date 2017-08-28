from django.forms import ModelForm
from lista.models import Post, Compra


class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = ('fecha_compra',)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('producto', 'precio')