#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#################################################################
# USUARIO #######################################################
#################################################################

class Rol_Usuario(models.Model):
	id_rol = models.AutoField(primary_key=True)
	rol = models.CharField(max_length=50, unique=True)
	descripcion = models.CharField(max_length=100, null=True, blank=True)

	def __unicode__(self):
		return "%s" % (self.rol,)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class Usuario(models.Model):
	id_usuario = models.AutoField(primary_key=True)
	usuario = models.OneToOneField(User) #REQUERIDO
	primer_nombre = models.CharField(max_length=50) #REQUERIDO
	segundo_nombre = models.CharField(max_length=50, null=True, blank=True)
	primer_apellido = models.CharField(max_length=50) #REQUERIDO
	segundo_apellido = models.CharField(max_length=50, null=True, blank=True)
	correo = models.EmailField() #REQUERIDO
	rol = models.ForeignKey(Rol_Usuario, null=True, blank=True) #REQUERIDO
	activo = models.BooleanField(default=True)
	fecha_creacion =  models.DateTimeField(auto_now_add=True)
	ultima_conexion = models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
			return "%s %s - (%s)" % (self.primer_nombre, self.primer_apellido, self.usuario)

#################################################################
# CLIENTES ######################################################
#################################################################

class Cliente(models.Model):
	id_cliente = models.AutoField(primary_key=True)
	rif = models.CharField(max_length=10, unique=True) #REQUERIDO
	cliente = models.CharField(max_length=100) #REQUERIDO
	direccion = models.TextField(max_length=150) #REQUERIDO
	telefono_1 = models.CharField(max_length=15) #REQUERIDO
	telefono_2 = models.CharField(max_length=15, null=True, blank=True) 	
	fax = models.CharField(max_length=15, null=True, blank=True)
	correo = models.EmailField(null=True, blank=True)
	iva = models.BooleanField(default=False)
		
	def __unicode__(self):
		return "%s - %s" % (self.rif,self.cliente,)

#################################################################
# PRODUCTOS #####################################################
#################################################################

class Tipo_Producto(models.Model):
	id_tipo_producto = models.AutoField(primary_key=True)
	tipo_producto = models.CharField(max_length=50, unique=True)
	descripcion = models.TextField(null=True, blank=True)
	
	def __unicode__(self):
		return "%s" % (self.tipo_producto,)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class Producto(models.Model):
	id_producto = models.AutoField(primary_key=True)
	codigo = models.CharField(max_length=10, unique=True) #REQUERIDO
	producto = models.CharField(max_length=100, unique=True) #REQUERIDO
	tipo_producto = models.ForeignKey(Tipo_Producto) #REQUERIDO
	descripcion = models.TextField(null=True, blank=True, default=None)
	precio_unitario = models.DecimalField(max_digits=12, decimal_places=2) #REQUERIDO
	
	def __unicode__(self):
		return "%s" % (self.producto,)

#################################################################
# INVENTARIO ####################################################
#################################################################

class Stock(models.Model):
	id_stock = models.AutoField(primary_key=True)
	producto_id = models.IntegerField() #REQUERIDO
	codigo_producto = models.CharField(max_length=10, unique=True) #REQUERIDO
	nombre_producto = models.CharField(max_length=100, unique=True) #REQUERIDO
	cantidad_producto = models.IntegerField() #REQUERIDO

	def __unicode__(self):
		return "%s" % (self.nombre_producto,)

#################################################################
# VENTAS ########################################################
#################################################################

class Venta(models.Model):
	id_venta = models.AutoField(primary_key=True)
	cliente = models.ForeignKey(Cliente) #REQUERIDO
	producto = models.ForeignKey(Producto) #REQUERIDO
	cantidad = models.IntegerField() #REQUERIDO
	total_venta = models.DecimalField(max_digits=12, decimal_places=2) #REQUERIDO
	fecha_venta = models.DateTimeField(auto_now_add=True)

#################################################################
# ESTADISTICAS ##################################################
#################################################################

class Utilidad_Mensual(models.Model):
	id_utilidad_mensual = models.AutoField(primary_key=True)
	ano = models.IntegerField(unique=True) #REQUERIDO
	ene = models.IntegerField(null=True, blank=True)
	feb = models.IntegerField(null=True, blank=True)
	mar = models.IntegerField(null=True, blank=True)
	abr = models.IntegerField(null=True, blank=True)
	may = models.IntegerField(null=True, blank=True)
	jun = models.IntegerField(null=True, blank=True)
	jul = models.IntegerField(null=True, blank=True)
	ago = models.IntegerField(null=True, blank=True)
	sep = models.IntegerField(null=True, blank=True)
	oct = models.IntegerField(null=True, blank=True)
	nov = models.IntegerField(null=True, blank=True)
	dic = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return "%s" % (self.ano,)

#################################################################
# EMPLEADOS #####################################################
#################################################################

class Cargo(models.Model):
	id_cargo = models.AutoField(primary_key=True)
	cargo = models.CharField(max_length=50, unique=True) #REQUERIDO
	descripcion = models.CharField(max_length=100, null=True, blank=True)
	
	def __unicode__(self):
		return "%s" % (self.cargo,)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class Tipo_Empleado(models.Model):
	id_tipo_empleado = models.AutoField(primary_key=True)
	tipo_empleado = models.CharField(max_length=50) #REQUERIDO
	descripcion = models.CharField(max_length=100, null=True, blank=True)
	
	def __unicode__(self):
		return "%s" % (self.tipo_empleado,)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class Empleado(models.Model):
	id_empleado = models.AutoField(primary_key=True)
	cedula = models.CharField(max_length=10, unique=True) #REQUERIDO
	primer_nombre = models.CharField(max_length=50) #REQUERIDO
	segundo_nombre = models.CharField(max_length=50, null=True, blank=True)
	primer_apellido = models.CharField(max_length=50) #REQUERIDO
	segundo_apellido = models.CharField(max_length=50, null=True, blank=True)
	telefono_local = models.CharField(max_length=15, null=True, blank=True) 
	telefono_celular = models.CharField(max_length=15) #REQUERIDO
	fecha_nacimiento = models.DateField(null=True, blank=True, default=None)
	direccion = models.TextField(max_length=150) #REQUERIDO
	correo_personal = models.EmailField() #REQUERIDO
	correo_corporativo = models.EmailField(null=True, blank=True)
	sueldo = models.DecimalField(max_digits=12, decimal_places=2)
	cargo = models.ForeignKey(Cargo) #REQUERIDO
	tipo_empleado = models.ForeignKey(Tipo_Empleado) #REQUERIDO
	fecha_ingreso = models.DateField() #REQUERIDO
	fecha_egreso = models.DateField(null=True, blank=True)
	
	def __unicode__(self):
		return "%s - %s %s" % (self.cedula,self.primer_nombre,self.primer_apellido,)