#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#############
#  USUARIO 	#
#############

class Rol_Usuario(models.Model):
	id_rol = models.AutoField(primary_key=True)
	rol = models.CharField(max_length=50, unique=True)
	descripcion = models.CharField(max_length=100, null=True, blank=True, default=None)

	def __unicode__(self):
		return "%s" % (self.rol,)


class Usuario(models.Model):
	id_usuario = models.AutoField(primary_key=True)
	usuario = models.OneToOneField(User)
	primer_nombre = models.CharField(max_length=50)
	segundo_nombre = models.CharField(max_length=50, null=True, blank=True, default=None)
	primer_apellido = models.CharField(max_length=50)
	segundo_apellido = models.CharField(max_length=50, null=True, blank=True, default=None)
	correo = models.EmailField()
	rol = models.ForeignKey(Rol_Usuario, null=True, blank=True, default=None) #Hacer requerido
	activo = models.BooleanField(default=True)
	fecha_creacion =  models.DateTimeField(auto_now_add=True)
	ultima_conexion = models.DateTimeField(null=True, blank=True, default=None)

	def __unicode__(self):
			return "%s %s - (%s)" % (self.primer_nombre, self.primer_apellido, self.usuario)


###########
# CLIENTE #
###########


class Cliente(models.Model):
	id_cliente = models.AutoField(primary_key=True)
	rif = models.CharField(max_length=10, unique=True)
	cliente = models.CharField(max_length=100)
	direccion = models.TextField(null=True, blank=True, default=None)
	telefono_1 = models.CharField(max_length=15)
	telefono_2 = models.CharField(max_length=15, null=True, blank=True, default=None) 	
	fax = models.CharField(max_length=15, null=True, blank=True, default=None)
	correo = models.EmailField(null=True, blank=True, default=None)
	iva = models.BooleanField(default=False)
		
	def __unicode__(self):
		return "%s - %s" % (self.rif,self.cliente,)

##############
# INVENTARIO #
##############


class Tipo_Producto(models.Model):
	id_tipo_producto = models.AutoField(primary_key=True)
	tipo_producto = models.CharField(max_length=50, unique=True)
	descripcion = models.TextField(null=True, blank=True, default=None)
	
	def __unicode__(self):
		return "%s" % (self.tipo_producto,)

class Producto(models.Model):
	id_producto = models.AutoField(primary_key=True)
	codigo = models.CharField(max_length=10, unique=True)
	producto = models.CharField(max_length=100, unique=True)
	tipo_producto = models.ForeignKey(Tipo_Producto, null=True, blank=True, default=None) #Hacer requerido
	descripcion = models.TextField(null=True, blank=True, default=None)
	precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
	
	def __unicode__(self):
		return "%s" % (self.producto,)

class Inventario(models.Model):
	id_inventario = models.AutoField(primary_key=True)
	codigo_producto = models.CharField(max_length=10, unique=True)
	nombre_producto = models.CharField(max_length=100, unique=True)
	cantidad_producto = models.IntegerField()
	precio_producto = models.DecimalField(max_digits=12, decimal_places=2)
	precio_total = models.DecimalField(max_digits=12, decimal_places=2)

	def __unicode__(self):
		return "%s" % (self.nombre_producto,)

class Venta(models.Model):
	id_venta = models.AutoField(primary_key=True)
	cliente = models.ForeignKey(Cliente)
	producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField()
	fecha_venta = models.DateTimeField(auto_now_add=True)


###############
# ESTADISTICA #
###############

class Utilidad_Mensual(models.Model):
	id_utilidad_mensual = models.AutoField(primary_key=True)
	ano = models.IntegerField(unique=True)
	ene = models.IntegerField(null=True, blank=True, default=None)
	feb = models.IntegerField(null=True, blank=True, default=None)
	mar = models.IntegerField(null=True, blank=True, default=None)
	abr = models.IntegerField(null=True, blank=True, default=None)
	may = models.IntegerField(null=True, blank=True, default=None)
	jun = models.IntegerField(null=True, blank=True, default=None)
	jul = models.IntegerField(null=True, blank=True, default=None)
	ago = models.IntegerField(null=True, blank=True, default=None)
	sep = models.IntegerField(null=True, blank=True, default=None)
	oct = models.IntegerField(null=True, blank=True, default=None)
	nov = models.IntegerField(null=True, blank=True, default=None)
	dic = models.IntegerField(null=True, blank=True, default=None)

	def __unicode__(self):
		return "%s" % (self.ano,)

############
# EMPLEADO #
############

class Cargo(models.Model):
	id_cargo = models.AutoField(primary_key=True)
	cargo = models.CharField(max_length=50, unique=True)
	descripcion = models.CharField(max_length=100, null=True, blank=True, default=None)
	
	def __unicode__(self):
		return "%s" % (self.cargo,)

class Tipo_Empleado(models.Model):
	id_tipo_empleado = models.AutoField(primary_key=True)
	tipo_empleado = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100, null=True, blank=True, default=None)
	
	def __unicode__(self):
		return "%s" % (self.estatus_empleado,)

class Empleado(models.Model):
	id_empleado = models.AutoField(primary_key=True)
	cedula = models.CharField(max_length=10, unique=True)
	primer_nombre = models.CharField(max_length=50)
	segundo_nombre = models.CharField(max_length=50, null=True, blank=True, default=None)
	primer_apellido = models.CharField(max_length=50)
	segundo_apellido = models.CharField(max_length=50, null=True, blank=True, default=None)
	telefono_1 = models.CharField(max_length=15)
	telefono_2 = models.CharField(max_length=15, null=True, blank=True, default=None) 
	fecha_nacimiento = models.DateField(null=True)
	direccion = models.TextField(null=True, blank=True, default=None)
	correo = models.EmailField(null=True, blank=True, default=None)
	sueldo = models.DecimalField(max_digits=12, decimal_places=2)
	cargo = models.ForeignKey(Cargo, null=True, blank=True, default=None) 
	fecha_ingreso = models.DateField()
	fecha_egreso = models.DateField(null=True, blank=True, default=None)
	tipo_empleado = models.ForeignKey(Tipo_Empleado, null=True, blank=True, default=None)
	
	def __unicode__(self):
		return "%s - %s %s" % (self.cedula,self.primer_nombre,self.primer_apellido,)