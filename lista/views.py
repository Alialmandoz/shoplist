from django.shortcuts import render, redirect
from lista.forms import PostForm, CompraForm

# Create your views here.
from lista.models import Post, Compra


def index(request):
    return render(request, 'index.html')


def crear_post(request):

    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    else:
        form = CompraForm()
    return render(request, 'post/crear_post.html', {'form': form})


def add_product(request, pk):
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            prod_added = form.save(commit=False)
            prod_added.orden = orden
            prod_added = form.save()
            return redirect('orden', pk=orden.pk)
            return render(request, 'post/detalle_post.html', {'posts': posts})
    else:
        form = PostForm()
    return render(request, 'post/add_product.html', {'form': form})



def detalle_post(request):
    posts = Post.objects.all()
    return render(request, 'post/detalle_post.html', {'posts': posts})


def buscar_post(request):
    return render(request, 'post/buscar_post.html')


def editar_post(request, pk):
    return render(request, 'post/editar_post.html')


def borrar_post(request, pk):
    return render(request, 'post/borrar_post.html')


def alerta_borrar_post(request):
    return render(request, 'post/alerta_borrar_post.html')