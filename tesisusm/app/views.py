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

#################################################################
# INICIO_PRIVADO

class Dashboard(TemplateView):
	template_name = 'dashboard.html'

	def get_context_data (self, **kwargs):
		context = super(Dashboard, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['cliente'] = Cliente.objects.all()
		context['producto'] = Producto.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#################################################################
# CONFIGURACION #################################################
#################################################################

#################################################################
#VER PERFIL

class VerPerfil(DetailView):
	template_name = 'perfil/perfil_ver.html'
	model = Usuario
	context_object_name = 'usuario'

	def get_context_data (self, **kwargs):
		context = super(VerPerfil, self).get_context_data(**kwargs)
		context['now'] = datetime.datetime.now()
		return context

#################################################################
#EDITAR PERFIL

class UpdatePerfil(UpdateView):
	template_name = 'perfil/perfil_editar.html'
	model = Usuario
	form_class = UserFormUpdate
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

#################################################################
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

#################################################################
# VER USUARIOS

class VerUsuario(DetailView):
	template_name = 'usuario/usuario_ver.html'
	model = Usuario
	context_object_name = 'usuario'

	def get_context_data (self, **kwargs):
		context = super(VerUsuario, self).get_context_data(**kwargs)
		context['now'] = datetime.datetime.now()
		return context

#################################################################
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

#################################################################
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

#################################################################
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

#################################################################
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

#################################################################
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

#################################################################
# REGISTRAR CLIENTE

class RegClientes(FormView):
	template_name = 'cliente/cliente_registro.html'
	form_class = ClienteForm
	success_url = reverse_lazy('lista_clientes')

	def form_valid (self, form):
		cliente = form.save()
		return super(RegClientes, self).form_valid(form)

	def get_context_data (self, **kwargs):
		context = super(RegClientes, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#################################################################
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

#################################################################
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

#################################################################
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

#################################################################
# VER PRODUCTOS

class VerProductos(DetailView):
	template_name = 'producto/producto_ver.html'
	model = Producto
	context_object_name = 'producto'

	def get_context_data (self, **kwargs):
		context = super(VerProductos, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#################################################################
#REGISTRAR PRODUCTO

class RegProductos(FormView):
	template_name = 'producto/producto_registro.html'
	form_class = ProductoForm
	success_url = reverse_lazy('lista_productos')

	def form_valid (self, form):
		producto = form.save()
		return super(RegProductos, self).form_valid(form)

	def get_context_data (self, **kwargs):
		context = super(RegProductos, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#################################################################
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

#################################################################
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

#################################################################
# INVENTARIO

class Inventario(ListView):
	template_name = 'inventario/inventario_lista.html'
	model = Inventario
	context_object_name = 'inventario'

	def get_context_data (self, **kwargs):
		context = super(Inventario, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

#################################################################
#EDITAR PRODUCTO INVENTARIO

class EditProdInventario(DetailView):
	template_name = 'inventario/inventario_lista.html'
	model = Inventario
	context_object_name = 'producto'

	"""
	form_class = InventarioForm
	success_url = reverse_lazy('inventario')

	def get_context_data (self, **kwargs):
		context = super(EditProdInventario, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context
	"""

#################################################################
# EMPLEADOS	#####################################################
#################################################################

#LISTA_EMPLEADOS
class Empleados(ListView):
	template_name = 'empleado_lista.html'
	model = Empleado
	context_object_name = 'empleado'

	def get_context_data (self, **kwargs):
		context = super(Empleados, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context


#REGISTRO_EMPLEADOS
class RegEmpleados(FormView):
	template_name = 'empleado_registro.html'
	form_class = EmpleadoForm
	success_url = reverse_lazy('lista_empleados')

	def form_valid (self, form):
		empleado = form.save()
		return super(RegEmpleados, self).form_valid(form)

	def get_context_data (self, **kwargs):
		context = super(RegEmpleados, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context


#EDITAR_EMPLEADOS
class UpdateEmpleado(UpdateView):
	template_name = 'empleado_editar.html'
	model = Empleado
	form_class = EmpleadoForm
	success_url = reverse_lazy('lista_empleados')

	def get_context_data (self, **kwargs):
		context = super(UpdateEmpleado, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context


#BORRAR_EMPLEADOS
class DeleteEmpleado(DeleteView):
	template_name = 'empleado_eliminar.html'
	model = Empleado
	success_url = reverse_lazy('lista_empleados')

	def get_context_data (self, **kwargs):
		context = super(DeleteEmpleado, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context


#############
#   VENTA	#
#############
	
#LISTA_VENTAS	
class Ventas(ListView):
	template_name = 'venta_lista.html'
	model = Venta
	context_object_name = 'venta'

	def get_context_data (self, **kwargs):
		context = super(Ventas, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context

	
#REGSITRO_VENTAS
class RegVentas(FormView):
	template_name = 'venta_registro.html'
	form_class = VentaForm
	success_url = reverse_lazy('lista_ventas')

	def form_valid (self, form):
		venta = form.save()
		return super(RegVentas, self).form_valid(form)

	def get_context_data (self, **kwargs):
		context = super(RegVentas, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context


#EDITAR_VENTAS
class UpdateVenta(UpdateView):
	template_name = 'venta_editar.html'
	model = Venta
	form_class = VentaForm
	success_url = reverse_lazy('lista_ventas')

	def get_context_data (self, **kwargs):
		context = super(UpdateVenta, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context


#BORRAR_VENTAS
class DeleteVenta(DeleteView):
	template_name = 'venta_eliminar.html'
	model = Venta
	success_url = reverse_lazy('lista_ventas')

	def get_context_data (self, **kwargs):
		context = super(DeleteVenta, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context


#############
#  GRAFICA	#
#############

#ESTADISTICA / GRAFICA
class Estadisticas(ListView):
	template_name = 'estadistica.html'
	model = Utilidad_Mensual
	context_object_name = 'utilidad'

	def get_context_data (self, **kwargs):
		context = super(Estadisticas, self).get_context_data(**kwargs)
		context['usuario'] = Usuario.objects.all()
		context['now'] = datetime.datetime.now()
		return context