from django.contrib import admin
from django.contrib.admin import AdminSite
from encodings import search_function
from web.models import *


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre','descripcion','cantidad',)
    ordering = ('codigo',)
    search_fields = ('codigo',)
admin.site.register(Productos,ProductoAdmin)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto','correo',)
    ordering = ('nombre',)
admin.site.register(Empresa,EmpresaAdmin)


