from django.contrib import admin
from lista.models import Compra


class CompraAdmin(admin.ModelAdmin):
    model = Compra
    list_display = ('producto', 'fecha_compra')

# Register your models here.
admin.site.register(Compra, CompraAdmin)
