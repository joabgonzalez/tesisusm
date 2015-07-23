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
    #PUBLICO
    url(r'^$', Index.as_view(), name='inicio'),
    url(r'^registro/$', RegUsuarios.as_view(), name='registro_usuario'),
    #LOGIN
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    #LOGOUT
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    #PRIVADO
    url(r'^main/$', login_required(Main.as_view()), name='main'),
    url(r'^usuarios/$', login_required(Usuarios.as_view()), name='lista_usuarios'),
    url(r'^usuarios/registrar$', login_required(RegUsuarios.as_view()), name='registro_usuarios_priv'),
    url(r'^productos/$', login_required(Productos.as_view()), name='lista_productos'),
    url(r'^productos/registrar$', login_required(RegProductos.as_view()), name='registro_productos'),
    url(r'^empleados$', login_required(Empleados.as_view()), name='lista_empleados'),
    url(r'^empleados/registrar$', login_required(RegEmpleados.as_view()), name='registro_empleados'),
]   