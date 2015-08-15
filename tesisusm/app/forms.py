#encoding: utf-8
from django import forms
from models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	nombres = forms.CharField(max_length=50)
	apellidos = forms.CharField(max_length=50)
	correo_electronico = forms.EmailField(max_length=50)


class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		exclude = ('status',)
		widgets = {
				'cod_prod': forms.TextInput(attrs={'class': 'form-control'}),
				'nb_prod': forms.TextInput(attrs={'class': 'form-control'}),
				'id_tipo_prod': forms.Select(attrs={'class': 'form-control'}),
				'desc_prod': forms.TextInput(attrs={'class': 'form-control'}),
				'precio_prod': forms.TextInput(attrs={'class': 'form-control'}),					
		}
		labels = {
				'cod_prod': ("Código"),
				'nb_prod': ("Nombre"),
				'id_tipo_prod': ("Tipo de producto"),
				'desc_prod': ("Descripción"),
				'precio_prod': ("Precio"),
		}
		

class EmpleadoForm(ModelForm):
	class Meta:
		model = Empleado
		exclude = ('status',)
		widgets = {
				'ci': forms.TextInput(attrs={'class': 'form-control'}),
				'nb_1': forms.TextInput(attrs={'class': 'form-control'}),
				'nb_2': forms.TextInput(attrs={'class': 'form-control'}),
				'ap_1': forms.TextInput(attrs={'class': 'form-control'}),
				'ap_2': forms.TextInput(attrs={'class': 'form-control'}),
				'tlf1': forms.TextInput(attrs={'class': 'form-control'}),
				'cel': forms.TextInput(attrs={'class': 'form-control'}),
				'fe_nac': forms.TextInput(attrs={'class': 'form-control'}),
				'mail': forms.TextInput(attrs={'class': 'form-control'}),
				'direccion': forms.TextInput(attrs={'class': 'form-control'}),
				'sueldo': forms.TextInput(attrs={'class': 'form-control'}),
				'id_cargo': forms.Select(attrs={'class': 'form-control'}),
				'fe_ingreso': forms.DateInput(attrs={'class': 'form-control'}),
				'fe_egreso': forms.DateInput(attrs={'class': 'form-control'}),
						
		}
		labels = {
				'ci': ("Cédula de Identidad"),
				'nb_1': ("Primer Nombre"),
				'nb_2': ("Segundo Nombre"),
				'ap_1': ("Primer Apellido"),
				'ap_2': ("Segundo Apellido"),
				'tlf1': ("Teléfono"),
				'cel': ("Móvil"),
				'fe_nac': ("Fecha de Nacimiento"),
				'mail': ("E-mail"),
				'direccion': ("Dirección"),
				'sueldo': ("Sueldo"),
				'id_cargo': ("Cargo"),
				'fe_ingreso': ("Fecha de Ingreso"),
				'fe_egreso': ("Fecha de Egreso"),
		}
		
		
class VentaForm(ModelForm):
	class Meta:
		model = Venta
		exclude = ('status',)
		widgets = {
				'cliente': forms.Select(attrs={'class': 'form-control'}),
				'producto': forms.Select(attrs={'class': 'form-control'}),
				'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
				'fe_venta': forms.DateInput(attrs={'class': 'form-control'}),
					
		}
		labels = {
				'cliente': ("Cliente"),
				'producto': ("Producto"),
				'cantidad': ("Cantidad"),
				'fe_venta': ("Fecha de Venta"),
		}
		
	
class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		exclude = ('status',)
		widgets = {
				'rif': forms.TextInput(attrs={'class': 'form-control'}),
				'nb_cliente': forms.TextInput(attrs={'class': 'form-control'}),
				'dir_cliente': forms.TextInput(attrs={'class': 'form-control'}),
				'tlf1': forms.TextInput(attrs={'class': 'form-control'}),
				'tlf2': forms.TextInput(attrs={'class': 'form-control'}),
				'fax': forms.TextInput(attrs={'class': 'form-control'}),
				'mail': forms.TextInput(attrs={'class': 'form-control'}),
				'iva': forms.CheckboxInput(attrs={'class': 'checkbox'}),
				
		}
		labels = {
				'rif': ("RIF o CI"),
				'dir_cliente': ("Dirección"),
				'nb_cliente': ("Nombre o Razón Social"),
				'tlf1': ("Teléfono 1"),
				'tlf2': ("Teléfono 2"),
				'fax': ("Fax"),
				'mail': ("Correo Electrónico"),
				'iva': ("Aplica IVA"),
	 	}