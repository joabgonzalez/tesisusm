#encoding: utf-8
from django.views.generic import TemplateView, FormView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse_lazy
from forms import *

# Create your views here.

#INICIO_PUBLICO
class Index(TemplateView):
	template_name = 'index.html'


#REGISTRO_USUARIO_PUBLICO
class RegUsuariosPub(FormView):
	template_name = 'reg_usuario_pub.html'
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


#LISTA_USUARIOS_VISTA_PRIVADA
class Usuarios(ListView):
	template_name = 'lista_usuario_priv.html'
	model = Usuario
	context_object_name = 'usuario'

	
#REGISTRO_USUARIO_PRIVADO
class RegUsuariosPriv(FormView):
	template_name = 'reg_usuario_priv.html'
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


#INICIO_PRIVADO
class Dashboard(TemplateView):
	template_name = 'dashboard.html'


#LISTA_PRODUCTOS
class Productos(ListView):
	template_name = 'lista_producto.html'
	model = Producto
	context_object_name = 'producto'


#REGISTRAR_PRODUCTO
class RegProductos(FormView):
	template_name = 'reg_producto.html'
	form_class = ProductoForm
	success_url = reverse_lazy('lista_productos')

	def form_valid (self, form):
		producto = form.save()
		return super(RegProductos, self).form_valid(form)

#EDITAR_PRODUCTO
class UpdateProducto(UpdateView):
	template_name = 'editar_producto.html'
	model = Producto
	form_class = ProductoForm
	success_url = reverse_lazy('lista_productos')

#BORRAR_PRODUCTO
class DeleteProducto(DeleteView):
	template_name = 'eliminar_producto.html'
	model = Producto
	success_url = reverse_lazy('lista_productos')


#LISTA_EMPLEADOS
class Empleados(ListView):
	template_name = 'lista_empleado.html'
	model = Empleado
	context_object_name = 'empleado'


#REGISTRO_EMPLEADOS
class RegEmpleados(FormView):
	template_name = 'reg_empleado.html'
	form_class = EmpleadoForm
	success_url = reverse_lazy('lista_empleados')

	def form_valid (self, form):
		empleado = form.save()
		return super(RegEmpleados, self).form_valid(form)

	
#LISTA_VENTAS	
class Ventas(ListView):
	template_name = 'lista_venta.html'
	model = Venta
	context_object_name = 'venta'	

	
#REGSITRO_VENTAS
class RegVentas(FormView):
	template_name = 'reg_venta.html'
	form_class = VentaForm
	success_url = reverse_lazy('ventas')

	def form_valid (self, form):
		venta = form.save()
		return super(RegVentas, self).form_valid(form)

	
#LISTA_VENTAS	
class Clientes(ListView):
	template_name = 'lista_cliente.html'
	model = Cliente
	context_object_name = 'cliente'

		
#REGSITRO_CLIENTES	
class RegClientes(FormView):
	template_name = 'reg_cliente.html'
	form_class = ClienteForm
	success_url = reverse_lazy('lita_clientes')

	def form_valid (self, form):
		cliente = form.save()
		return super(RegClientes, self).form_valid(form)


#ESTADISTICA / GRAFICA
class Estadisticas(TemplateView):
	template_name = 'estadistica.html'