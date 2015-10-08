#encoding: utf-8
from django.views.generic import TemplateView, FormView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from forms import *
import datetime
from django.contrib.auth.models import User

#################################################################
# DASHBOARD #####################################################
#################################################################

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# INICIO_PRIVADO

class Dashboard(TemplateView):
	template_name = 'dashboard.html'

	def get_context_data (self, **kwargs):
		context = super(Dashboard, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['cliente'] = Cliente.objects.all()
		context['producto'] = Producto.objects.all()
		context['inventario'] = Stock.objects.all()
		context['venta'] = Venta.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#################################################################
# CONFIGURACION #################################################
#################################################################

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#VER PERFIL

class VerPerfil(DetailView):
	template_name = 'perfil/perfil_ver.html'
	model = Usuario
	context_object_name = 'usuario'

	def get_context_data (self, **kwargs):
		context = super(VerPerfil, self).get_context_data(**kwargs)
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#EDITAR PERFIL

class UpdatePerfil(UpdateView):
	template_name = 'perfil/perfil_editar.html'
	model = Usuario
	form_class = PerfilForm
	success_url = reverse_lazy('ver_perfil')

	def form_valid (self, form):
		usuario = form.save()
		return super(UpdatePerfil, self).form_valid(form)

	def get_context_data (self, **kwargs):
		context = super(UpdatePerfil, self).get_context_data(**kwargs)
		context['now'] = datetime.datetime.now()
		return context

#################################################################
# USUARIO #######################################################
#################################################################

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# LISTA USUARIOS

class Usuarios(ListView):
	template_name = 'usuario/usuario_lista.html'
	model = Usuario
	context_object_name = 'usuario'

	def get_context_data (self, **kwargs):
		context = super(Usuarios, self).get_context_data(**kwargs)
		context['perfil'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# VER USUARIOS

class VerUsuario(DetailView):
	template_name = 'usuario/usuario_ver.html'
	model = Usuario
	context_object_name = 'usuario'

	def get_context_data (self, **kwargs):
		context = super(VerUsuario, self).get_context_data(**kwargs)
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# REGISTRO USUARIO

class RegUsuario(FormView):
	template_name = 'usuario/usuario_registro.html'
	form_class = UserForm
	success_url = reverse_lazy('lista_usuarios')

	def form_valid (self, form):
		user = form.save()
		u = Usuario()
		u.usuario = user
		u.primer_nombre = form.cleaned_data['primer_nombre']
		u.segundo_nombre = form.cleaned_data['segundo_nombre']
		u.primer_apellido = form.cleaned_data['primer_apellido']
		u.segundo_apellido = form.cleaned_data['segundo_apellido']
		u.correo = form.cleaned_data['correo_electronico']
		u.save()
		return super(RegUsuario, self).form_valid(form)

	def get_context_data (self, **kwargs):
		context = super(RegUsuario, self).get_context_data(**kwargs)
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#EDITAR USUARIO

class UpdateUsuario(UpdateView):
	template_name = 'usuario/usuario_editar.html'
	model = Usuario
	form_class = UserFormUpdate
	success_url = reverse_lazy('lista_usuarios')

	def form_valid (self, form):
		usuario = form.save()
		return super(UpdateUsuario, self).form_valid(form)

	def get_context_data (self, **kwargs):
		context = super(UpdateUsuario, self).get_context_data(**kwargs)
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#ELIMINAR USUARIO

class DeleteUsuario(DeleteView):
	template_name = 'usuario/usuario_eliminar.html'
	model = Usuario
	context_object_name = 'usuario'
	success_url = reverse_lazy('lista_usuarios')

	def get_context_data (self, **kwargs):
		context = super(DeleteUsuario, self).get_context_data(**kwargs)
		context['now'] = datetime.datetime.now()
		return context

#################################################################
# CLIENTES ######################################################
#################################################################

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# LISTA CIENTES

class Clientes(ListView):
	template_name = 'cliente/cliente_lista.html'
	model = Cliente
	context_object_name = 'cliente'

	def get_context_data (self, **kwargs):
		context = super(Clientes, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# VER CIENTES

class VerCliente(DetailView):
	template_name = 'cliente/cliente_ver.html'
	model = Cliente
	context_object_name = 'cliente'

	def get_context_data (self, **kwargs):
		context = super(VerCliente, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# REGISTRAR CLIENTE

class RegCliente(FormView):
	template_name = 'cliente/cliente_registro.html'
	form_class = ClienteForm
	success_url = reverse_lazy('lista_clientes')

	def form_valid (self, form):
		cliente = form.save()
		return super(RegCliente, self).form_valid(form)

	def get_context_data (self, **kwargs):
		context = super(RegCliente, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# EDITAR CLIENTE

class UpdateCliente(UpdateView):
	template_name = 'cliente/cliente_editar.html'
	model = Cliente
	form_class = ClienteForm
	success_url = reverse_lazy('lista_clientes')

	def get_context_data (self, **kwargs):
		context = super(UpdateCliente, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# BORRAR CLIENTE

class DeleteCliente(DeleteView):
	template_name = 'cliente/cliente_eliminar.html'
	model = Cliente
	context_object_name = 'cliente'
	success_url = reverse_lazy('lista_clientes')

	def get_context_data (self, **kwargs):
		context = super(DeleteCliente, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#################################################################
# PRODUCTOS	#####################################################
#################################################################

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# LISTA PRODUCTOS

class Productos(ListView):
	template_name = 'producto/producto_lista.html'
	model = Producto
	context_object_name = 'producto'

	def get_context_data (self, **kwargs):
		context = super(Productos, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# VER PRODUCTOS

class VerProducto(DetailView):
	template_name = 'producto/producto_ver.html'
	model = Producto
	context_object_name = 'producto'

	def get_context_data (self, **kwargs):
		context = super(VerProducto, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#REGISTRAR PRODUCTO

class RegProducto(FormView):
	template_name = 'producto/producto_registro.html'
	form_class = ProductoForm
	success_url = reverse_lazy('lista_productos')

	def form_valid (self, form):
		producto = form.save()
		return super(RegProducto, self).form_valid(form)

	def get_context_data (self, **kwargs):
		context = super(RegProducto, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#EDITAR PRODUCTO

class UpdateProducto(UpdateView):
	template_name = 'producto/producto_editar.html'
	model = Producto
	form_class = ProductoForm
	success_url = reverse_lazy('lista_productos')

	def get_context_data (self, **kwargs):
		context = super(UpdateProducto, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#BORRAR PRODUCTO

class DeleteProducto(DeleteView):
	template_name = 'producto/producto_eliminar.html'
	model = Producto
	context_object_name = 'producto'
	success_url = reverse_lazy('lista_productos')

	def get_context_data (self, **kwargs):
		context = super(DeleteProducto, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#################################################################
# INVENTARIO ####################################################
#################################################################

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# INVENTARIO

class Inventario(ListView):
	template_name = 'inventario/inventario_lista.html'
	model = Stock
	context_object_name = 'inventario'

	def get_context_data (self, **kwargs):
		context = super(Inventario, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#EDITAR CANTIDAD PRODUCTO

class EditProdInventario(UpdateView):
	template_name = 'inventario/inventario_editar.html'
	model = Stock
	form_class = InventarioForm
	success_url = reverse_lazy('inventario')

	def get_context_data (self, **kwargs):
		context = super(EditProdInventario, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#AGREGAR PRODUCTO

class AddProdInventario(UpdateView):
	template_name = 'inventario/inventario_agregar.html'
	model = Stock
	form_class = InventarioAddForm
	success_url = reverse_lazy('inventario')

	def get_context_data (self, **kwargs):
		context = super(AddProdInventario, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#################################################################
# VENTA	#########################################################
#################################################################

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#LISTA VENTAS

class Ventas(ListView):
	template_name = 'venta/venta_lista.html'
	model = Venta
	context_object_name = 'venta'

	def get_context_data (self, **kwargs):
		context = super(Ventas, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#VER VENTAS

class VerVenta(DetailView):
	template_name = 'venta/venta_ver.html'
	model = Venta
	context_object_name = 'venta'

	def get_context_data (self, **kwargs):
		context = super(VerVenta, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#REGSITRO VENTAS

class RegVenta(FormView):
	template_name = 'venta/venta_registro.html'
	form_class = VentaForm
	success_url = reverse_lazy('lista_ventas')

	def form_valid (self, form):
		venta = form.save()
		return super(RegVenta, self).form_valid(form)

	def get_context_data (self, **kwargs):
		context = super(RegVenta, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

from django.core import serializers
from django.http import HttpResponse

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#AJAX DE PRODUCTOS EN LA VENTA

class VentaProdAjax(TemplateView):

	def get (self, request, *args, **kwargs):
		id_prod = request.GET['id']
		querie = Producto.objects.filter(id_producto=id_prod)
		data = serializers.serialize('json', querie, fields=('precio_unitario',))
		return HttpResponse(data, content_type='application/json')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#AJAX DE STOCK EN LA VENTA

class VentaInvAjax(TemplateView):

	def get (self, request, *args, **kwargs):
		id_prod = request.GET['id_inv']
		querie = Stock.objects.filter(producto_id=id_prod)
		data = serializers.serialize('json', querie, fields=('cantidad_producto',))
		return HttpResponse(data, content_type='application/json')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#EDITAR VENTAS

class UpdateVenta(UpdateView):
	template_name = 'venta/venta_editar.html'
	model = Venta
	form_class = VentaEditForm
	success_url = reverse_lazy('lista_ventas')

	def get_context_data (self, **kwargs):
		context = super(UpdateVenta, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#ELIMINAR VENTAS

class DeleteVenta(DeleteView):
	template_name = 'venta/venta_eliminar.html'
	model = Venta
	context_object_name = 'venta'
	success_url = reverse_lazy('lista_ventas')

	def get_context_data (self, **kwargs):
		context = super(DeleteVenta, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#################################################################
# ESTADISTICAS	#################################################
#################################################################

#ESTADISTICA / GRAFICA
class Estadisticas(ListView):
	template_name = 'estadistica/estadistica.html'
	model = Utilidad_Mensual
	context_object_name = 'utilidad'

	def get_context_data (self, **kwargs):
		context = super(Estadisticas, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#################################################################
# EMPLEADOS	#####################################################
#################################################################

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#LISTA EMPLEADOS

class Empleados(ListView):
	template_name = 'empleado/empleado_lista.html'
	model = Empleado
	context_object_name = 'empleado'

	def get_context_data (self, **kwargs):
		context = super(Empleados, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#VER EMPLEADOS

class VerEmpleado(DetailView):
	template_name = 'empleado/empleado_ver.html'
	model = Empleado
	context_object_name = 'empleado'

	def get_context_data (self, **kwargs):
		context = super(VerEmpleado, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#REGISTRO EMPLEADOS

class RegEmpleado(FormView):
	template_name = 'empleado/empleado_registro.html'
	form_class = EmpleadoForm
	success_url = reverse_lazy('lista_empleados')

	def form_valid (self, form):
		empleado = form.save()
		return super(RegEmpleado, self).form_valid(form)

	def get_context_data (self, **kwargs):
		context = super(RegEmpleado, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#EDITAR EMPLEADOS

class UpdateEmpleado(UpdateView):
	template_name = 'empleado/empleado_editar.html'
	model = Empleado
	form_class = EmpleadoEditForm
	success_url = reverse_lazy('lista_empleados')

	def get_context_data (self, **kwargs):
		context = super(UpdateEmpleado, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#BORRAR EMPLEADOS

class DeleteEmpleado(DeleteView):
	template_name = 'empleado/empleado_eliminar.html'
	model = Empleado
	context_object_name = 'empleado'
	success_url = reverse_lazy('lista_empleados')

	def get_context_data (self, **kwargs):
		context = super(DeleteEmpleado, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context