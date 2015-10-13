#encoding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from app.views import *
from django.contrib.auth.forms import AdminPasswordChangeForm

urlpatterns = [
	#ADMIN
	url(r'^admin/', include(admin.site.urls)),
	#LOGIN/INICIO
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'index.html'}, name='inicio'),
	#LOGOUT
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	#DASHBOARD
	url(r'^dashboard/$', login_required(Dashboard.as_view()), name='dashboard'),
	#CONFIGURACION
	url(r'^perfil/(?P<pk>[0-9]+)/ver$', login_required(VerPerfil.as_view()), name='ver_perfil'),
	url(r'^perfil/(?P<pk>[0-9]+)/editar$', login_required(UpdatePerfil.as_view()), name='editar_perfil'),
	#USUARIO
	url(r'^usuarios/$', login_required(Usuarios.as_view()), name='lista_usuarios'),
	url(r'^usuarios/ver/(?P<pk>[0-9]+)/$', login_required(VerUsuario.as_view()), name='ver_usuarios'),
	url(r'^usuarios/registrar$', login_required(RegUsuario.as_view()), name='registro_usuarios'),
	url(r'^usuarios/editar/(?P<pk>[0-9]+)/$', login_required(UpdateUsuario.as_view()), name='editar_usuarios'),
	url(r'^usuarios/(?P<pk>[0-9]+)/eliminar$', login_required(DeleteUsuario.as_view()), name='eliminar_usuarios'),
	#CLIENTES
	url(r'^clientes$', login_required(Clientes.as_view()), name='lista_clientes'),
	url(r'^clientes/ver/(?P<pk>[0-9]+)/$', login_required(VerCliente.as_view()), name='ver_cliente'),
	url(r'^clientes/registrar$', login_required(RegCliente.as_view()), name='registro_clientes'),
	url(r'^clientes/editar/(?P<pk>[0-9]+)/$', login_required(UpdateCliente.as_view()), name='editar_clientes'),
	url(r'^clientes/(?P<pk>[0-9]+)/eliminar$', login_required(DeleteCliente.as_view()), name='eliminar_clientes'),
	#PRODUCTO
	url(r'^productos/$', login_required(Productos.as_view()), name='lista_productos'),
	url(r'^productos/ver/(?P<pk>[0-9]+)/$', login_required(VerProducto.as_view()), name='ver_productos'),
	url(r'^productos/registrar$', login_required(RegProducto.as_view()), name='registro_productos'),
	url(r'^productos/editar/(?P<pk>[0-9]+)/$', login_required(UpdateProducto.as_view()), name='editar_productos'),
	url(r'^productos/(?P<pk>[0-9]+)/eliminar$', login_required(DeleteProducto.as_view()), name='eliminar_productos'),
	#INVENTARIO
	url(r'^inventario/$', login_required(Inventario.as_view()), name='inventario'),
	url(r'^inventario/(?P<pk>[0-9]+)/editar$', login_required(EditProdInventario.as_view()), name='editar_inventario'),
	url(r'^inventario/agregar/(?P<pk>[0-9]+)$', login_required(AddProdInventario.as_view()), name='agregar_inventario'),
	#VENTAS
	url(r'^ventas$', login_required(Ventas.as_view()), name='lista_ventas'),
	url(r'^ventas/ver/(?P<pk>[0-9]+)/$', login_required(VerVenta.as_view()), name='ver_ventas'),
	url(r'^ventas/registrar$', login_required(RegVenta.as_view()), name='registro_ventas'),
	url(r'^ventas/registrar/producto_ajax/$', login_required(VentaProdAjax.as_view())), #ModuloAjax
	url(r'^ventas/registrar/stock_ajax/$', login_required(VentaInvAjax.as_view())), #ModuloAjax
	url(r'^ventas/editar/(?P<pk>[0-9]+)/$', login_required(UpdateVenta.as_view()), name='editar_ventas'),
	url(r'^ventas/(?P<pk>[0-9]+)/eliminar$', login_required(DeleteVenta.as_view()), name='eliminar_ventas'),
	#ESTADISTICAS
	url(r'^estadisticas/$', login_required(Estadisticas.as_view()), name='estadisticas'),
	url(r'^estadisticas/ventas$', login_required(EstadisticasVentas.as_view()), name='estadisticas_ventas'),
	url(r'^proyecciones/$', login_required(Proyecciones.as_view()), name='proyecciones'),
	url(r'^proyecciones/ventas$', login_required(ProyeccionesVentas.as_view()), name='proyecciones_ventas'),
	#EMPLEADOS
	url(r'^empleados$', login_required(Empleados.as_view()), name='lista_empleados'),
	url(r'^empleados/ver/(?P<pk>[0-9]+)/$', login_required(VerEmpleado.as_view()), name='ver_empleados'),
	url(r'^empleados/registrar$', login_required(RegEmpleado.as_view()), name='registro_empleados'),
	url(r'^empleados/editar/(?P<pk>[0-9]+)/$', login_required(UpdateEmpleado.as_view()), name='editar_empleados'),
	url(r'^empleados/(?P<pk>[0-9]+)/eliminar$', login_required(DeleteEmpleado.as_view()), name='eliminar_empleados'),
]