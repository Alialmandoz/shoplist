from django.conf.urls import url
from . import views

urlpatterns = [
    # inicio
    url(r'^$', views.index, name='index'),

    # ########################## post ########################## #

    # Crear cliente
    url(r'^crear_post/$', views.crear_post, name='crear_post'),
    #
    # add product
    url(r'^agregar/(?P<pk>[-\d]+)/$', views.agregar, name='agregar'),

    # add new product

    url(r'^cargarproducto/$', views.cargar_producto, name='cargar_producto'),

    # detalle de post
    url(r'^detalle/(?P<pk>[-\d]+)/$', views.detalle_compra, name='detalle_compra'),
    #
    # buscar post
    url(r'^post/buscar/$', views.buscar_post, name='buscar_post'),

    # editar post
    url(r'^detalle/(?P<pk>[-\d]+)/edit/$', views.editar_compra, name='editar_compra'),
    #
    # Borrar cliente
    url(r'^detalle/(?P<pk>[-\d]+)/edit/borrar/$', views.borrar_post, name='borrar_post'),
    #
    # alerta Borrar cliente
    url(r'^detalle/(?P<pk>[-\d]+)/edit/alerta/$', views.alerta_borrar_post, name='alerta_borrar_post'),
    #
    #
    # # contacto
    # url(r'^contacto/$', views.contacto, name='contacto'),

]