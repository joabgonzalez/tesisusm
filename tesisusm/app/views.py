#encoding: utf-8
from django.views.generic import TemplateView, FormView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from forms import *

# Create your views here.


#############
#	INDEX 	#
#############

#INICIO_PUB
class Index(TemplateView):
	template_name = 'index.html'


#############
# DASHBOARD #
#############

#INICIO_PRIV
class Dashboard(TemplateView):
	template_name = 'dashboard.html'


#############
#  USUARIO 	#
#############

#LISTA_USUARIOS_PRIV
class Usuarios(ListView):
	template_name = 'usuario_lista.html'
	model = Usuario
	context_object_name = 'usuario'


#REGISTRO_USUARIO_PUB
class RegUsuariosPub(FormView):
	template_name = 'usuario_registro_pub.html'
	form_class = UserForm
	success_url = reverse_lazy('inicio')

	def form_valid (self, form):
		user = form.save()
		usuario = Usuario()
		usuario.usuario = user
		usuario.nombre = form.cleaned_data['nombres']
		usuario.apellido = form.cleaned_data['apellidos']
		usuario.correo = form.cleaned_data['correo_electronico']
		usuario.save()
		return super(RegUsuariosPub, self).form_valid(form)

	
#REGISTRO_USUARIO_PRIV
class RegUsuariosPriv(FormView):
	template_name = 'usuario_registro_priv.html'
	form_class = UserForm
	success_url = reverse_lazy('lista_usuarios_priv')

	def form_valid (self, form):
		user = form.save()
		usuario = Usuario()
		usuario.usuario = user
		usuario.nombre = form.cleaned_data['nombres']
		usuario.apellido = form.cleaned_data['apellidos']
		usuario.correo = form.cleaned_data['correo_electronico']
		usuario.save()
		return super(RegUsuariosPriv, self).form_valid(form)

class UpdateUsuario(UpdateView):
	template_name = 'usuario_editar.html'
	#model = Usuario
	form_class = UserForm
	#fields = ['nombre', 'apellido', 'correo']
	success_url = reverse_lazy('lista_usuarios_priv')


#############
# PRODUCTOS	#
#############

#LISTA_PRODUCTOS
class Productos(ListView):
	template_name = 'producto_lista.html'
	model = Producto
	context_object_name = 'producto'


#REGISTRAR_PRODUCTO
class RegProductos(FormView):
	template_name = 'producto_registro.html'
	form_class = ProductoForm
	success_url = reverse_lazy('lista_productos')

	def form_valid (self, form):
		producto = form.save()
		return super(RegProductos, self).form_valid(form)

#EDITAR_PRODUCTO
class UpdateProducto(UpdateView):
	template_name = 'producto_editar.html'
	model = Producto
	form_class = ProductoForm
	success_url = reverse_lazy('lista_productos')


#BORRAR_PRODUCTO
class DeleteProducto(DeleteView):
	template_name = 'producto_eliminar.html'
	model = Producto
	success_url = reverse_lazy('lista_productos')


#############
# EMPLEADOS	#
#############

#LISTA_EMPLEADOS
class Empleados(ListView):
	template_name = 'empleado_lista.html'
	model = Empleado
	context_object_name = 'empleado'


#REGISTRO_EMPLEADOS
class RegEmpleados(FormView):
	template_name = 'empleado_registro.html'
	form_class = EmpleadoForm
	success_url = reverse_lazy('lista_empleados')

	def form_valid (self, form):
		empleado = form.save()
		return super(RegEmpleados, self).form_valid(form)


#EDITAR_EMPLEADOS
class UpdateEmpleado(UpdateView):
	template_name = 'empleado_editar.html'
	model = Empleado
	form_class = EmpleadoForm
	success_url = reverse_lazy('lista_empleados')


#BORRAR_EMPLEADOS
class DeleteEmpleado(DeleteView):
	template_name = 'empleado_eliminar.html'
	model = Empleado
	success_url = reverse_lazy('lista_empleados')


#############
#   VENTA	#
#############
	
#LISTA_VENTAS	
class Ventas(ListView):
	template_name = 'venta_lista.html'
	model = Venta
	context_object_name = 'venta'	

	
#REGSITRO_VENTAS
class RegVentas(FormView):
	template_name = 'venta_registro.html'
	form_class = VentaForm
	success_url = reverse_lazy('lista_ventas')

	def form_valid (self, form):
		venta = form.save()
		return super(RegVentas, self).form_valid(form)


#EDITAR_VENTAS
class UpdateVenta(UpdateView):
	template_name = 'venta_editar.html'
	model = Venta
	form_class = VentaForm
	success_url = reverse_lazy('lista_ventas')


#BORRAR_VENTAS
class DeleteVenta(DeleteView):
	template_name = 'venta_eliminar.html'
	model = Venta
	success_url = reverse_lazy('lista_ventas')


#############
#  CIENTES	#
#############
	
#LISTA_CIENTES
class Clientes(ListView):
	template_name = 'cliente_lista.html'
	model = Cliente
	context_object_name = 'cliente'

		
#REGSITRO_CLIENTES
class RegClientes(FormView):
	template_name = 'cliente_registro.html'
	form_class = ClienteForm
	success_url = reverse_lazy('lista_clientes')

	def form_valid (self, form):
		cliente = form.save()
		return super(RegClientes, self).form_valid(form)


#EDITAR_CLIENTES
class UpdateCliente(UpdateView):
	template_name = 'cliente_editar.html'
	model = Cliente
	form_class = ClienteForm
	success_url = reverse_lazy('lista_clientes')


#BORRAR_CLIENTES
class DeleteCliente(DeleteView):
	template_name = 'cliente_eliminar.html'
	model = Cliente
	success_url = reverse_lazy('lista_clientes')


#############
#  GRAFICA	#
#############

#ESTADISTICA / GRAFICA
class Estadisticas(TemplateView):
	template_name = 'estadistica.html'