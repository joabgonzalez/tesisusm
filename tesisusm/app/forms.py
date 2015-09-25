#encoding: utf-8
from django import forms
from models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	primer_nombre = forms.CharField(
		max_length=50,
		label='Primer nombre',
		widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre'}),

	)
	segundo_nombre = forms.CharField(
		max_length=50,
		required=False,
		label='Segundo nombre',
		widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo nombre'}),
	)
	primer_apellido = forms.CharField(
		max_length=50,
		label='Primer apellido',
		widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer apellido'}),
	)
	segundo_apellido = forms.CharField(
		max_length=50,
		required=False,
		label='Segundo apellido',
		widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo apellido'}),
	)
	correo_electronico = forms.EmailField(
		max_length=50,
		label='Correo electrónico',
		widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
	)
	password1 = forms.CharField(
		label='Contraseña',
		required = True, 
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
	)
	password2 = forms.CharField(
		label='Confirmar contraseña',
		required = True,
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
	)

	class Meta:
		model = User
		#exclude = ('password','last_login','groups','user_permissions','date_joined','is_superuser',)
		fields = ('username','password1','password2',)
		widgets = {
				'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
		}

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['username'].help_text = False

#################################################################

class UserFormUpdate(ModelForm):
	class Meta:
		model = Usuario
		exclude = ('usuario_id','ultima_conexion')
		widgets = {
				'usuario': forms.Select(attrs={'class': 'form-control', 'disabled': 'disabled'}),
				'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre'}),
				'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seundo nombre'}),
				'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer apellido'}),
				'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo apellido'}),
				'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
				'rol': forms.Select(attrs={'class': 'form-control'}),
		}
		labels = {
				'usuario': ("Usuario"),
				'primer_nombre': ("Primer nombre"),
				'segundo_nombre': ("Segundo nombre"),
				'primer_apellido': ("Primer apellido"),
				'segundo_apellido': ("Segundo apellido"),
				'correo': ("Correo electónico"),
				'activo': ('Usuario activo'),
				'rol': ('Rol de usuario'),
		}
		

	def __init__(self, *args, **kwargs):
		super(UserFormUpdate, self).__init__(*args, **kwargs)
		self.fields['usuario'].required = False
		self.fields['segundo_nombre'].required = False
		self.fields['segundo_apellido'].required = False

#################################################################

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		exclude = ('status',)
		widgets = {
				'rif': forms.TextInput(attrs={'class': 'form-control'}),
				'cliente': forms.TextInput(attrs={'class': 'form-control'}),
				'direccion': forms.TextInput(attrs={'class': 'form-control'}),
				'telefono_1': forms.TextInput(attrs={'class': 'form-control'}),
				'telefono_2': forms.TextInput(attrs={'class': 'form-control'}),
				'fax': forms.TextInput(attrs={'class': 'form-control'}),
				'correo': forms.TextInput(attrs={'class': 'form-control'}),
				
		}
		labels = {
				'rif': ("RIF o CI"),
				'direccion': ("Dirección"),
				'cliente': ("Nombre o Razón Social"),
				'telefono_1': ("Teléfono Principal"),
				'telefono_2': ("Teléfono Segundario"),
				'fax': ("Fax"),
				'correo': ("Correo Electrónico"),
				'iva': ("Aplica IVA"),
		}

#################################################################

class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		exclude = ()
		widgets = {
				'codigo': forms.TextInput(attrs={'class': 'form-control'}),
				'producto': forms.TextInput(attrs={'class': 'form-control'}),
				'tipo_producto': forms.Select(attrs={'class': 'form-control'}),
				'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
				'precio_unitario': forms.TextInput(attrs={'class': 'form-control'}),
		}
		labels = {
				'codigo': ("Código"),
				'producto': ("Producto"),
				'tipo_producto': ("Tipo de producto"),
				'descripcion': ("Descripción"),
				'precio_unitario': ("Precio unitario (Bs)"),
		}

#################################################################

class InventarioForm(ModelForm):
	class Meta:
		model = Inventario
		exclude = ('codigo_producto','nombre_producto','precio_producto','precio_total')
		widgets = {
				'cantidad_producto': forms.TextInput(attrs={'class': 'form-control'}),
		}
		labels = {
				'cantidad_producto': ("Producto"),
		}

#################################################################	

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

#################################################################

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