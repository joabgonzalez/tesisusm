#encoding: utf-8
from django import forms
from models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	primer_nombre = forms.CharField(
		max_length=50,
		label='* Primer nombre',
		widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre del usuario'}),

	)
	segundo_nombre = forms.CharField(
		max_length=50,
		required=False,
		label='Segundo nombre',
		widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seundo nombre del usuario'}),
	)
	primer_apellido = forms.CharField(
		max_length=50,
		label='* Primer apellido',
		widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer apellido del usuario'}),
	)
	segundo_apellido = forms.CharField(
		max_length=50,
		required=False,
		label='Segundo apellido',
		widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo apellido del usuario'}),
	)
	correo_electronico = forms.EmailField(
		max_length=50,
		label='* Correo electrónico',
		widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico del usuario'}),
	)
	password1 = forms.CharField(
		label='* Contraseña',
		required = True, 
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
	)
	password2 = forms.CharField(
		label='* Confirmar contraseña',
		required = True,
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}),
	)

	class Meta:
		model = User
		#exclude = ('password','last_login','groups','user_permissions','date_joined','is_superuser',)
		fields = ('username','password1','password2',)
		widgets = {
				'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
		}
		labels = {
				'username': ("* Usuario"),
		}


	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['username'].help_text = False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class UserFormUpdate(ModelForm):
	class Meta:
		model = Usuario
		exclude = ('usuario_id','ultima_conexion')
		widgets = {
				'usuario': forms.Select(attrs={'class': 'form-control', 'disabled': 'disabled'}),
				'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre del usuario'}),
				'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seundo nombre del usuario'}),
				'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer apellido del usuario'}),
				'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo apellido del usuario'}),
				'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico del usuario'}),
				'rol': forms.Select(attrs={'class': 'form-control'}),
		}
		labels = {
				'usuario': ("Usuario"),
				'primer_nombre': ("* Primer nombre"),
				'segundo_nombre': ("Segundo nombre"),
				'primer_apellido': ("* Primer apellido"),
				'segundo_apellido': ("Segundo apellido"),
				'correo': ("* Correo electónico"),
				'activo': ('Usuario activo'),
				'rol': ('* Rol de usuario'),
		}
		

	def __init__(self, *args, **kwargs):
		super(UserFormUpdate, self).__init__(*args, **kwargs)
		self.fields['usuario'].required = False
		self.fields['segundo_nombre'].required = False
		self.fields['segundo_apellido'].required = False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class PerfilForm(ModelForm):
	class Meta:
		model = Usuario
		exclude = ('usuario_id','ultima_conexion','rol', 'activo')
		widgets = {
				'usuario': forms.Select(attrs={'class': 'form-control', 'disabled': 'disabled'}),
				'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre del usuario'}),
				'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seundo nombre del usuario'}),
				'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer apellido del usuario'}),
				'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo apellido del usuario'}),
				'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico del usuario'}),
		}
		labels = {
				'usuario': ("Usuario"),
				'primer_nombre': ("* Primer nombre"),
				'segundo_nombre': ("Segundo nombre"),
				'primer_apellido': ("* Primer apellido"),
				'segundo_apellido': ("Segundo apellido"),
				'correo': ("* Correo electónico"),
		}
		

	def __init__(self, *args, **kwargs):
		super(PerfilForm, self).__init__(*args, **kwargs)
		self.fields['usuario'].required = False
		self.fields['segundo_nombre'].required = False
		self.fields['segundo_apellido'].required = False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		exclude = ('status',)
		widgets = {
				'rif': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de RIF del cliente'}),
				'cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Razon social del cliente'}),
				'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Domicilio fiscal del cliente'}),
				'telefono_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono de contacto'}),
				'telefono_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono alternativo de contacto'}),
				'fax': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fax del cliente'}),
				'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico del cliente'}),
				
		}
		labels = {
				'rif': ("* CI o RIF"),
				'cliente': ("* Nombre o Razón Social"),
				'direccion': ("* Dirección"),
				'telefono_1': ("* Teléfono Principal"),
				'telefono_2': ("Teléfono Segundario"),
				'fax': ("Fax"),
				'correo': ("Correo Electrónico"),
				'iva': ("Aplica IVA"),
		}

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		exclude = ()
		widgets = {
				'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código del producto'}),
				'producto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
				'tipo_producto': forms.Select(attrs={'class': 'form-control'}),
				'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción del producto'}),
				'precio_unitario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Precio del producto por unidad (Bs)'}),
		}
		labels = {
				'codigo': ("* Código"),
				'producto': ("* Producto"),
				'tipo_producto': ("* Tipo de producto"),
				'descripcion': ("Descripción"),
				'precio_unitario': ("* Precio unitario (Bs)"),
		}

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class InventarioForm(ModelForm):
	class Meta:
		model = Stock
		exclude = ('codigo_producto','producto_id')
		widgets = {
				'nombre_producto': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
				'cantidad_producto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad disponible del producto'}),
		}
		labels = {
				'nombre_producto': ("Nombre del producto"),
				'cantidad_producto': ("* Cantidad del producto"),
		}

	def __init__(self, *args, **kwargs):
		super(InventarioForm, self).__init__(*args, **kwargs)
		self.fields['nombre_producto'].required = False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class VentaForm(ModelForm):
	class Meta:
		model = Venta
		exclude = ('fecha_venta',)
		widgets = {
				'cliente': forms.Select(attrs={'class': 'form-control'}),
				'producto': forms.Select(attrs={'class': 'form-control'}),
				'cantidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad del producto a vender'}),
				'total_venta': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled', 'placeholder': 'Total de la venta'}),
					
		}
		labels = {
				'cliente': ("* Cliente"),
				'producto': ("* Producto"),
				'cantidad': ("* Cantidad"),
				'total_venta': ("Total"),

		}

	def __init__(self, *args, **kwargs):
		super(VentaForm, self).__init__(*args, **kwargs)
		self.fields['total_venta'].required = False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class VentaEditForm(ModelForm):
	class Meta:
		model = Venta
		exclude = ('fecha_venta',)
		widgets = {
				'cliente': forms.Select(attrs={'class': 'form-control', 'disabled': 'disabled'}),
				'producto': forms.Select(attrs={'class': 'form-control', 'disabled': 'disabled'}),
				'cantidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad del producto a vender'}),
				'total_venta': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
					
		}
		labels = {
				'cliente': ("Cliente"),
				'producto': ("Producto"),
				'cantidad': ("* Cantidad"),
				'total_venta': ("Total"),

		}

	def __init__(self, *args, **kwargs):
		super(VentaEditForm, self).__init__(*args, **kwargs)
		self.fields['cliente'].required = False
		self.fields['producto'].required = False
		self.fields['total_venta'].required = False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#	

class EmpleadoForm(ModelForm):
	class Meta:
		model = Empleado
		exclude = ('fecha_egreso', 'correo_corporativo')
		widgets = {
				'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cédula de identidad del empleado'}),
				'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre del empleado'}),
				'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo nombre del empleado'}),
				'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer apellido del empleado'}),
				'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo apellido del empleado'}),
				'telefono_local': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono de habitación del empleado'}),
				'telefono_celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono móvil del empleado'}),
				'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de nacimiento del empleado'}),
				'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
				'correo_personal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico del empleado'}),
				'sueldo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sueldo del empleado'}),
				'cargo': forms.Select(attrs={'class': 'form-control'}),
				'tipo_empleado': forms.Select(attrs={'class': 'form-control'}),
				'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de ingreso'}),
						
		}
		labels = {
				'cedula': ("* Cédula de identidad"),
				'primer_nombre': ("* Primer nombre"),
				'segundo_nombre': ("Segundo nombre"),
				'primer_apellido': ("* Primer apellido"),
				'segundo_apellido': ("Segundo apellido"),
				'telefono_local': ("Teléfono de habitación"),
				'telefono_celular': ("* Teléfono móvil"),
				'fecha_nacimiento': ("Fecha de nacimiento"),
				'direccion': ("* Dirección"),
				'correo_personal': ("* Correo personal"),
				'sueldo': ("* Sueldo"),
				'cargo': ("* Cargo"),
				'tipo_empleado': ("* Tipo de empleado"),
				'fecha_ingreso': ("* Fecha de ingreso"),
		}

		def __init__(self, *args, **kwargs):
			super(EmpleadoForm, self).__init__(*args, **kwargs)
			self.fields['segundo_nombre'].required = False
			self.fields['segundo_apellido'].required = False
			self.fields['telefono_local'].required = False
			self.fields['fecha_nacimiento'].required = False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#	

class EmpleadoEditForm(ModelForm):
	class Meta:
		model = Empleado
		exclude = ()
		widgets = {
				'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cédula de identidad del empleado'}),
				'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre del empleado'}),
				'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo nombre del empleado'}),
				'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer apellido del empleado'}),
				'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo apellido del empleado'}),
				'telefono_local': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono de habitación del empleado'}),
				'telefono_celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono móvil del empleado'}),
				'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de nacimiento del empleado'}),
				'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del empleado'}),
				'correo_personal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico del empleado'}),
				'correo_corporativo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo corporativo'}),
				'sueldo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sueldo del empleado'}),
				'cargo': forms.Select(attrs={'class': 'form-control'}),
				'tipo_empleado': forms.Select(attrs={'class': 'form-control'}),
				'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de ingreso'}),
				'fecha_egreso': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de egreso'}),
						
		}
		labels = {
				'cedula': ("* Cédula de identidad"),
				'primer_nombre': ("* Primer nombre"),
				'segundo_nombre': ("Segundo nombre"),
				'primer_apellido': ("* Primer apellido"),
				'segundo_apellido': ("Segundo apellido"),
				'telefono_local': ("Teléfono de habitación"),
				'telefono_celular': ("* Teléfono móvil"),
				'fecha_nacimiento': ("Fecha de nacimiento"),
				'direccion': ("* Dirección"),
				'correo_personal': ("* Correo personal"),
				'correo_corporativo': ("Correo corporativo"),
				'sueldo': ("* Sueldo"),
				'cargo': ("* Cargo"),
				'tipo_empleado': ("* Tipo de empleado"),
				'fecha_ingreso': ("* Fecha de ingreso"),
				'fecha_egreso': ("Fecha de egreso"),
		}

		def __init__(self, *args, **kwargs):
			super(EmpleadoEditForm, self).__init__(*args, **kwargs)
			self.fields['segundo_nombre'].required = False
			self.fields['segundo_apellido'].required = False
			self.fields['telefono_local'].required = False
			self.fields['fecha_nacimiento'].required = False
			self.fields['correo_corporativo'].required = False
			self.fields['fecha_egreso'].required = False