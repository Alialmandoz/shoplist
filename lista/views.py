from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from lista.forms import PostForm, CompraForm, ProductoForm

# Create your views here.
from lista.models import Post, Compra, Producto


def index(request):
    compras = Compra.objects.all()
    
    listadecompras={}
    for compra in compras:
        listadecompras[compra] = compra.post_set.all()


    print(listadecompras)
    return render(request, 'index.html', {'listadecompras': listadecompras })


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


def detalle_compra(request, pk):
    compra = get_list_or_404(Post, compra=pk)
    post = Compra.objects.get(pk=pk)
    print('*********' + str(compra) + '*********')
    return render(request, 'post/detalle_compra.html', {'compra': compra, 'post': post})


def cargar_producto(request):
    productos = Producto.objects.all()
    compras = Compra.objects.all()
    form = ProductoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect('lista:index')
    return render(request, 'post/cargar_producto.html', {'form': form, 'productos': productos, 'compras': compras})


def buscar_post(request):
    return render(request, 'post/buscar_post.html')


def editar_compra(request, pk):
    compra = Post.objects.get(pk=pk)
    form = CompraForm(request.POST or None)

    return render(request, 'post/editar_compra.html')


def borrar_post(request, pk):
    return render(request, 'post/borrar_post.html')


def alerta_borrar_post(request):
    return render(request, 'post/alerta_borrar_post.html')
