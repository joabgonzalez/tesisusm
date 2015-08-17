#encoding: utf-8
"""tesisusm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from app.views import *

urlpatterns = [
	#ADMIN
	url(r'^admin/', include(admin.site.urls)),
	#INICIO
	#url(r'^$', Index.as_view(), name='inicio'),
	#LOGIN
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'index.html'}, name='inicio'),
	#LOGOUT
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	#DASHBOARD
	url(r'^dashboard/$', login_required(Dashboard.as_view()), name='dashboard'),
	#USUARIO
	url(r'^registro/$', RegUsuariosPub.as_view(), name='registro_usuario_pub'),
	url(r'^usuarios/$', login_required(Usuarios.as_view()), name='lista_usuarios_priv'),
	url(r'^usuarios/registrar$', login_required(RegUsuariosPriv.as_view()), name='registro_usuarios_priv'),
	#url(r'^usuarios/editar/(?P<pk>[0-9]+)/$', login_required(UpdateUsuario.as_view()), name='editar_usuarios_priv'),
	#url(r'^usuarios/(?P<pk>[0-9]+)/eliminar$', login_required(DeleteUsuario.as_view()), name='eliminar_usuarios_priv'),
	#PRODUCTO
	url(r'^productos/$', login_required(Productos.as_view()), name='lista_productos'),
	url(r'^productos/registrar$', login_required(RegProductos.as_view()), name='registro_productos'),
	url(r'^productos/editar/(?P<pk>[0-9]+)/$', login_required(UpdateProducto.as_view()), name='editar_productos'),
	url(r'^productos/(?P<pk>[0-9]+)/eliminar$', login_required(DeleteProducto.as_view()), name='eliminar_productos'),
	#EMPLEADOS
	url(r'^empleados$', login_required(Empleados.as_view()), name='lista_empleados'),
	url(r'^empleados/registrar$', login_required(RegEmpleados.as_view()), name='registro_empleados'),
	url(r'^empleados/editar/(?P<pk>[0-9]+)/$', login_required(UpdateEmpleado.as_view()), name='editar_empleados'),
	url(r'^empleados/(?P<pk>[0-9]+)/eliminar$', login_required(DeleteEmpleado.as_view()), name='eliminar_empleados'),
	#VENTAS
	url(r'^ventas$', login_required(Ventas.as_view()), name='lista_ventas'),
	url(r'^ventas/registrar$', login_required(RegVentas.as_view()), name='registro_ventas'),
	url(r'^ventas/editar/(?P<pk>[0-9]+)/$', login_required(UpdateVenta.as_view()), name='editar_ventas'),
	url(r'^ventas/(?P<pk>[0-9]+)/eliminar$', login_required(DeleteVenta.as_view()), name='eliminar_ventas'),
	#CLIENTES
	url(r'^clientes$', login_required(Clientes.as_view()), name='lista_clientes'),
	url(r'^clientes/registrar$', login_required(RegClientes.as_view()), name='registro_clientes'),
	url(r'^clientes/editar/(?P<pk>[0-9]+)/$', login_required(UpdateCliente.as_view()), name='editar_clientes'),
	url(r'^clientes/(?P<pk>[0-9]+)/eliminar$', login_required(DeleteCliente.as_view()), name='eliminar_clientes'),
	#ESTADISTICAS
	url(r'^estadisticas/$', login_required(Estadisticas.as_view()), name='estadisticas'),
]