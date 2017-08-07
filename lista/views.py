from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def crear_post(request):
    return render(request, 'post/crear_post.html')


def detalle_post(request, pk):
    print(pk)
    return render(request, 'post/detalle_post.html')


def buscar_post(request):
    return render(request, 'post/buscar_post.html')


def editar_post(request, pk):
    return render(request, 'post/editar_post.html')


def borrar_post(request, pk):
    return render(request, 'post/borrar_post.html')


def alerta_borrar_post(request):
    return render(request, 'post/alerta_borrar_post.html')