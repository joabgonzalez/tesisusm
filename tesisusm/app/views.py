from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.template.context import RequestContext
from django.shortcuts import render,render_to_response, get_object_or_404
from models import *
from forms import *
import datetime

# Create your views here.

def publico(request):
    now = datetime.datetime.now()
    template = "publico.html"
    return render_to_response(template, {'current_date': now},)

#Guardar registro en la bd
def registro(request):
	usuario = Usuario.objects.all()
	if request.method == 'POST':
		form = UsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
	else:
		form = UsuarioForm()

	template = "registro.html"
	return render_to_response(template,context_instance = RequestContext(request, locals()))

#Inicio de sesion
def login(request):
    template = "login.html"
    return render_to_response(template,)

def producto(request):
    producto = Producto.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/lista_producto.html")
    else:
        form = ProductoForm()

    template = "lista_producto.html"
    return render_to_response(template,context_instance = RequestContext(request, locals()))



