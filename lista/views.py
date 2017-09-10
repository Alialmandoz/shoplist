from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from lista.forms import PostForm, CompraForm

# Create your views here.
from lista.models import Post, Compra


def index(request):
    compras = get_list_or_404(Compra)
    return render(request, 'index.html', {'compras': compras})


def crear_post(request):
    form = CompraForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            compra = form.save()
            print(" ********************* compra creada exitosamente ********************* ")
            return redirect('lista:agregar', pk=compra.pk)
        else:
            print(" ********************* invalid form ********************* ")
            form = CompraForm()
    return render(request, 'post/crear_post.html', {'form': form})


def agregar(request, pk):
    compra = Compra.objects.get(pk=pk)
    productos = compra.post_set.all()
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            prod_added = form.save(commit=False)
            prod_added.compra = compra
            prod_added = form.save()
            print(" ********************* " + str(prod_added) + " agregado exitosamente ********************* ")
            return redirect('lista:agregar', pk=compra.pk)
    else:
        form = PostForm()

    return render(request, 'post/add_product.html', {'form': form, 'productos': productos})


def detalle_post(request, pk):
    posts = get_list_or_404(Post, compra=pk)
    print('*********' + str(posts) + '*********')
    return render(request, 'post/detalle_post.html', {'posts': posts})


def buscar_post(request):
    return render(request, 'post/buscar_post.html')


def editar_post(request, pk):
    return render(request, 'post/editar_post.html')


def borrar_post(request, pk):
    return render(request, 'post/borrar_post.html')


def alerta_borrar_post(request):
    return render(request, 'post/alerta_borrar_post.html')