#encoding: utf-8
from django.contrib import admin
from models import *

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Rol_Usuario)
admin.site.register(Producto)
admin.site.register(Tipo_Producto)
admin.site.register(Empleado)
admin.site.register(Cargo)
admin.site.register(Cliente)
admin.site.register(Venta)