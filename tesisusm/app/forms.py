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
		widget= forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Primer nombre del usuario.',
			'autocomplete': 'off',
			'data-toggle': 'tooltip', 
			'data-placement': 'top', 
			'title': 'Solo permite caracteres alfabéticos',
			}),
	)
	segundo_nombre = forms.CharField(
		max_length=50,
		required=False,
		label='Segundo nombre',
		widget= forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Seundo nombre del usuario.',
			'autocomplete': 'off',
			'data-toggle': 'tooltip', 
			'data-placement': 'top', 
			'title': 'Solo permite caracteres alfabéticos',
			}),
	)
	primer_apellido = forms.CharField(
		max_length=50,
		label='* Primer apellido',
		widget= forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Primer apellido del usuario.',
			'autocomplete': 'off',
			'data-toggle': 'tooltip', 
			'data-placement': 'top', 
			'title': 'Solo permite caracteres alfabéticos',
			}),
	)
	segundo_apellido = forms.CharField(
		max_length=50,
		required=False,
		label='Segundo apellido',
		widget= forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Segundo apellido del usuario.',
			'autocomplete': 'off',
			'data-toggle': 'tooltip', 
			'data-placement': 'top', 
			'title': 'Solo permite caracteres alfabéticos',
			}),
	)
	correo_electronico = forms.EmailField(
		max_length=50,
		label='* Correo electrónico',
		widget= forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Correo electrónico del usuario. Ejm: corre@picnikki.com',
			'autocomplete': 'off',
			'data-toggle': 'tooltip', 
			'data-placement': 'top', 
			'title': 'Debe ser una dirección de correo electrónico válida',
			}),
	)
	password1 = forms.CharField(
		label='* Contraseña',
		required = True, 
		widget=forms.PasswordInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Contraseña.',
			'autocomplete': 'off',
			'data-toggle': 'tooltip', 
			'data-placement': 'top', 
			'title': 'Debe contener entre 6 y 20 caracteres con al menos una mayuscula, una minuscula y un número'}),
	)
	password2 = forms.CharField(
		label='* Confirmar contraseña',
		required = True,
		widget=forms.PasswordInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Confirmar contraseña.',
			'autocomplete': 'off',
			'data-toggle': 'tooltip', 
			'data-placement': 'top', 
			'title': 'Debe ser igual a la contraseña ingresada en el campo anterior'}),
	)

	class Meta:
		model = User
		fields = ('username','password1','password2',)
		widgets = {
				'username': forms.TextInput(attrs={
					'class': 'form-control', 
					'autocomplete': 'off', 
					'placeholder': 'Usuario.', 
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfanuméricos guion medio (-) y guion bajo (_)'}),
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
				'usuario': forms.Select(attrs={
					'class': 'form-control', 
					'autocomplete': 'off',
					'disabled': 'disabled',
					}),
				'primer_nombre': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Primer nombre del usuario.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'segundo_nombre': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Seundo nombre del usuario.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'primer_apellido': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Primer apellido del usuario.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'segundo_apellido': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Segundo apellido del usuario.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'correo': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Correo electrónico del usuario. Ejm: correo@picknikki.com',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Debe ser una dirección de correo electrónico válida',
					}),
				'rol': forms.Select(attrs={
					'class': 'form-control',
					}),
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
		self.fields['rol'].empty_label = 'Seleccione un rol'

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class PerfilForm(ModelForm):
	class Meta:
		model = Usuario
		exclude = ('usuario_id','ultima_conexion','rol', 'activo')
		widgets = {
				'usuario': forms.Select(attrs={
					'class': 'form-control', 
					'disabled': 'disabled',
					}),
				'primer_nombre': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Primer nombre del usuario.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'segundo_nombre': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Seundo nombre del usuario.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'primer_apellido': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Primer apellido del usuario.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'segundo_apellido': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Segundo apellido del usuario.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'correo': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Correo electrónico del usuario.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Debe ser una dirección de correo electrónico válida',
					}),
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
				'rif': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Registro único de informacion fiscal del cliente. Ejm: J-12345678-9',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Debe ingresar un formato de RIF válido',
					}),
				'cliente': forms.TextInput(attrs={
					'class': 'form-control',
					'placeholder': 'Razon social del cliente. Ejm: Picnikki y Asociados C.A.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar caracteres alfanuméricos, comilla simple (\'), comillas dobles ("), guion medio (-), guion bajo (_), punto(.) y coma(,).'
					}),
				'direccion': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Domicilio fiscal del cliente.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar caracteres alfanumericos y numeral(#)',
					}),
				'telefono_1': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Teléfono principal del cliente. Ejm: 0212-1234567',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar digitos, no puede ser igual a ningun otro numero de teléfono suministrado en este formulario',
					}),
				'telefono_2': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Teléfono segundario del cliente. Ejm: 0416-1234567',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar números, no puede ser igual a ningun otro numero de teléfono suministrado en este formulario',
					}),
				'fax': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Número de fax del cliente. Ejm: 02127654321',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar números, no puede ser igual a ningun otro numero de teléfono suministrado en este formulario',
					}),
				'correo': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Correo electrónico del cliente. Ejmcorreo@picknikki.com',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Debe ser una dirección de correo electrónico válida',
					}),		
		}
		labels = {
				'rif': ("* RIF"),
				'cliente': ("* Nombre o razón social"),
				'direccion': ("* Dirección"),
				'telefono_1': ("* Teléfono principal"),
				'telefono_2': ("Teléfono segundario"),
				'fax': ("Fax"),
				'correo': ("* Correo electrónico"),
		}

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		exclude = ()
		widgets = {
				'codigo': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Código del producto. Ejm: PK-1234',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar números',
					}),
				'producto': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Nombre del producto',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar caracteres alfabéticos',
					}),
				'tipo_producto': forms.Select(attrs={
					'class': 'form-control'
					}),
				'descripcion': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Descripción del producto',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Permite ingresar caracteres alfanuméricos, comilla simple (\'), comillas dobles ("), guion medio (-), guion bajo (_) comas (,) y punto (.) ',
					}),
				'precio_unitario': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Precio del producto por unidad (Bs)',
					'autocomplete': 'off',
					'maxlength': '10',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar valores numericos y punto (.) para valores decimales. Solo admite dos decimales',
					}),
		}
		labels = {
				'codigo': ("* Código"),
				'producto': ("* Producto"),
				'tipo_producto': ("* Tipo de producto"),
				'descripcion': ("Descripción"),
				'precio_unitario': ("* Precio unitario (Bs)"),
		}

	def __init__(self, *args, **kwargs):
		super(ProductoForm, self).__init__(*args, **kwargs)
		self.fields['tipo_producto'].empty_label = 'Seleccione un tipo de producto'

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class InventarioForm(ModelForm):
	class Meta:
		model = Stock
		exclude = ('codigo_producto','producto_id')
		widgets = {
				'nombre_producto': forms.TextInput(attrs={
					'class': 'form-control', 
					'disabled': 'disabled',
					}),
				'cantidad_producto': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Cantidad de producto',
					'autocomplete': 'off',
					'maxlength': '3',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar digitos',
					}),
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

class InventarioAddForm(ModelForm):
	nuevo = forms.CharField(
		max_length=3,
		label='* Cantidad a agregar',
		widget= forms.TextInput(attrs={
			'class': 'form-control', 
			'placeholder': 'Cantidad a agregar del producto',
			'autocomplete': 'off',
			'id': 'id_nuevo',
			'data-toggle': 'tooltip', 
			'data-placement': 'top', 
			'title': 'Solo permite ingresar digitos',
			}),
	)
	class Meta:
		model = Stock
		exclude = ('codigo_producto','producto_id')
		widgets = {
				'nombre_producto': forms.TextInput(attrs={
					'class': 'form-control', 
					'disabled': 'disabled',
					}),
				'cantidad_producto': forms.TextInput(attrs={
					'class': 'form-control', 
					'disabled': 'disabled'
					}),
		}
		labels = {
				'nombre_producto': ("Nombre del producto"),
				'cantidad_producto': ("Cantidad del producto"),
		}

	def __init__(self, *args, **kwargs):
		super(InventarioAddForm, self).__init__(*args, **kwargs)
		self.fields['nombre_producto'].required = False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class VentaForm(ModelForm):
	class Meta:
		model = Venta
		exclude = ('fecha_venta',)
		widgets = {
				'cliente': forms.Select(attrs={
					'class': 'form-control',
					}),
				'producto': forms.Select(attrs={
					'class': 'form-control',
					}),
				'cantidad': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Cantidad del producto a vender',
					'autocomplete': 'off',
					'maxlength': '3',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar digitos',
					}),
				'total_venta': forms.TextInput(attrs={
					'class': 'form-control', 
					'disabled': 'disabled', 
					'placeholder': 'Total de la venta',
					}),			
		}
		labels = {
				'cliente': ("* Cliente"),
				'producto': ("* Producto"),
				'cantidad': ("* Cantidad"),
				'total_venta': ("Total (Bs)"),

		}

	def __init__(self, *args, **kwargs):
		super(VentaForm, self).__init__(*args, **kwargs)
		self.fields['total_venta'].required = False
		self.fields['cliente'].empty_label = 'Seleccione un cliente'
		self.fields['producto'].empty_label = 'Seleccione un producto'


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class VentaEditForm(ModelForm):
	class Meta:
		model = Venta
		exclude = ('fecha_venta',)
		widgets = {
				'cliente': forms.Select(attrs={
					'class': 'form-control', 
					'disabled': 'disabled',
					}),
				'producto': forms.Select(attrs={
					'class': 'form-control', 
					'disabled': 'disabled',
					}),
				'cantidad': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Cantidad del producto a vender',
					'autocomplete': 'off',
					'maxlength': '3',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar digitos',
					}),
				'total_venta': forms.TextInput(attrs={
					'class': 'form-control', 
					'disabled': 'disabled',
					}),			
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
				'cedula': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Cédula de identidad del empleado. Ejm:1234567',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar digitos',
					}),
				'primer_nombre': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Primer nombre del empleado',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'segundo_nombre': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Segundo nombre del empleado',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'primer_apellido': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Primer apellido del empleado',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'segundo_apellido': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Segundo apellido del empleado',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'telefono_local': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Teléfono de habitación del empleado. Ejm: 0212-1234567',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar digitos, no puede ser igual a ningun otro numero de teléfono suministrado en este formulario',
					}),
				'telefono_celular': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Teléfono móvil del empleado. Ejm: 0416-1234567',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar digitos, no puede ser igual a ningun otro numero de teléfono suministrado en este formulario',
					}),
				'fecha_nacimiento': forms.DateInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Fecha de nacimiento del empleado. Ejm: dd/mm/yyyy',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Debe ser una fecha válida',
					}),
				'direccion': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Dirección del empleado.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar caracteres alfanumericos y numeral(#)',
					}),
				'correo_personal': forms.TextInput(attrs={
					'class': 'form-control',
					'placeholder': 'Correo electrónico personal del empleado. Ejm: correo@picnikki.com',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Debe ser una dirección de correo electrónico válida',
					}),
				'sueldo': forms.TextInput(attrs={
					'class': 'form-control',
					'maxlength': '8',
					'placeholder': 'Sueldo del empleado. Ejm: 12345.01',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar valores numericos y punto (.) para valores decimales. Solo admite dos decimales',
					}),
				'cargo': forms.Select(attrs={
					'class': 'form-control',
					}),
				'tipo_empleado': forms.Select(attrs={
					'class': 'form-control',
					}),
				'fecha_ingreso': forms.DateInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Fecha de ingreso del empleado. Ejm: dd/mm/yyyy',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Debe ser una fecha válida',
					}),				
		}
		labels = {
				'cedula': ("* Cédula de identidad"),
				'primer_nombre': ("* Primer nombre"),
				'segundo_nombre': ("Segundo nombre"),
				'primer_apellido': ("* Primer apellido"),
				'segundo_apellido': ("Segundo apellido"),
				'telefono_local': ("Teléfono de habitación"),
				'telefono_celular': ("* Teléfono móvil"),
				'fecha_nacimiento': ("* Fecha de nacimiento"),
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
		self.fields['cargo'].empty_label = 'Seleccione un cargo'
		self.fields['tipo_empleado'].empty_label = 'Seleccione un tipo de empleado'

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#################################################################
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#	

class EmpleadoEditForm(ModelForm):
	class Meta:
		model = Empleado
		exclude = ()
		widgets = {
				'cedula': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Cédula de identidad del empleado. Ejm: 12345678',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar digitos',
					}),
				'primer_nombre': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Primer nombre del empleado.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'segundo_nombre': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Segundo nombre del empleado.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'primer_apellido': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Primer apellido del empleado.',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'segundo_apellido': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Segundo apellido del empleado',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite caracteres alfabéticos',
					}),
				'telefono_local': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Teléfono de habitación del empleado. Ejm: 0212-1234567',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar digitos, no puede ser igual a ningun otro numero de teléfono suministrado en este formulario',
					}),
				'telefono_celular': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Teléfono móvil del empleado. Ejm: 0416-1234567',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar digitos, no puede ser igual a ningun otro numero de teléfono suministrado en este formulario',
					}),
				'fecha_nacimiento': forms.DateInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Fecha de nacimiento del empleado. Ejm: dd/mm/yyyy',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Debe ser una fecha válida',
					}),
				'direccion': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Dirección del empleado',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar caracteres alfanumericos y numeral(#)',
					}),
				'correo_personal': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Correo electrónico del empleado. Ejm: correo@picnikki.com',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Debe ser una dirección de correo electrónico válida',
					}),
				'correo_corporativo': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Correo electrónico corporativo del empleado. Ejm: correo@picnikki.com',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Debe ser una dirección de correo electrónico válida',
					}),
				'sueldo': forms.TextInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Sueldo del empleado. Ejm: 12345.01',
					'maxlength': '8',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Solo permite ingresar valores numericos y punto (.) para valores decimales. Solo admite dos decimales',
					}),
				'cargo': forms.Select(attrs={
					'class': 'form-control',
					}),
				'tipo_empleado': forms.Select(attrs={
					'class': 'form-control',
					}),
				'fecha_ingreso': forms.DateInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Fecha de ingreso del empleado. Ejm: dd/mm/yyyy',
					'autocomplete': 'off',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Debe ser una fecha válida',
					}),
				'fecha_egreso': forms.DateInput(attrs={
					'class': 'form-control', 
					'placeholder': 'Fecha de egreso del empleado. Ejm: dd/mm/yyyy',
					'data-toggle': 'tooltip', 
					'data-placement': 'top', 
					'title': 'Debe ser una fecha válida',
					}),				
		}
		labels = {
				'cedula': ("* Cédula de identidad"),
				'primer_nombre': ("* Primer nombre"),
				'segundo_nombre': ("Segundo nombre"),
				'primer_apellido': ("* Primer apellido"),
				'segundo_apellido': ("Segundo apellido"),
				'telefono_local': ("Teléfono de habitación"),
				'telefono_celular': ("* Teléfono móvil"),
				'fecha_nacimiento': ("* Fecha de nacimiento"),
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
		self.fields['correo_corporativo'].required = False
		self.fields['fecha_egreso'].required = False
		self.fields['cargo'].empty_label = 'Seleccione un cargo'
		self.fields['tipo_empleado'].empty_label = 'Seleccione un tipo de empleado'