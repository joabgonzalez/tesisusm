#encoding: utf-8
from django.views.generic import TemplateView, FormView, ListView
from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse_lazy
from forms import *

# Create your views here.

#INICIO_PUBLICO
class Index(TemplateView):
	template_name = 'index.html'

#USUARIOS
class Usuarios(ListView):
	template_name = 'lista_usuario.html'
	model = Usuario
	context_object_name = 'usuario'

#REGISTRO_USUARIO
class RegUsuarios(FormView):
	template_name = 'reg_usuario.html'
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
		return super(RegUsuarios, self).form_valid(form)

#INICIO_PRIVADO
class Main(TemplateView):
	template_name = 'main.html'

#PRODUCTOS
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

#EMPLEADOS
class Empleados(ListView):
	template_name = 'lista_empleado.html'
	model = Empleado
	context_object_name = 'empleado'

#LISTA_EMPLEADOS
class RegEmpleados(FormView):
	template_name = 'reg_empleado.html'
	form_class = EmpleadoForm
	success_url = reverse_lazy('lista_empleados')

	def form_valid (self, form):
		producto = form.save()
		return super(RegEmpleados, self).form_valid(form)