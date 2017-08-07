from django.shortcuts import render, redirect
from lista.forms import PostForm

# Create your views here.
from lista.models import Post


def index(request):
    return render(request, 'index.html')


def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            posts = Post.objects.all()
            return render(request, 'post/detalle_post.html', {'posts': posts})
    else:
        form = PostForm()
    return render(request, 'post/crear_post.html', {'form': form})


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