#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rol_Usuario(models.Model):
	id_rol = models.AutoField(primary_key=True)
	nb_rol = models.CharField(max_length=50)
	desc_rol = models.CharField(max_length=100)

	def __unicode__(self):
		return "%s" % (self.nb_rol,)


class Usuario(models.Model):
	usuario = models.OneToOneField(User)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	correo = models.EmailField()
	id_rol = models.ForeignKey(Rol_Usuario, null=True, blank=True, default=None)
	fe_create =  models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s %s - (%s)" % (self.nombre, self.apellido, self.usuario)


class Tipo_Producto(models.Model):
	id_tipo_producto = models.AutoField(primary_key=True)
	nb_tipo_producto = models.CharField(max_length=50)
	
	def __unicode__(self):
		return "%s" % (self.nb_tipo_producto)


class Producto(models.Model):
	id_prod = models.AutoField(primary_key=True)
	cod_prod = models.CharField(max_length=10)
	nb_prod = models.CharField(max_length=100)
	id_tipo_prod = models.ForeignKey(Tipo_Producto, null=True, default=None)#HAY QUE REVISAR EL MODELO
	desc_prod = models.TextField()
	precio_prod = models.FloatField()
	status = models.CharField(max_length=1, default="1")
	
	def __unicode__(self):
		return "%s" % (self.nb_prod)


class Cargo(models.Model):
	id_cargo = models.AutoField(primary_key=True)
	nb_cargo = models.CharField(max_length=50)
	desc_cargo = models.CharField(max_length=100)
	
	def __unicode__(self):
		return "%s" % (self.nb_cargo)


class Empleado(models.Model):
	id_empleado = models.AutoField(primary_key=True)
	ci = models.CharField(max_length=50, unique=True)
	nb_1 = models.CharField(max_length=50)
	nb_2 = models.CharField(max_length=50)
	ap_1 = models.CharField(max_length=50)
	ap_2 = models.CharField(max_length=50)
	tlf1 = models.CharField(max_length=15)
	cel = models.CharField(max_length=15) 
	fe_nac = models.DateField(null=True)
	mail = models.EmailField(null=True, default=None)
	direccion = models.TextField(blank=True)
	sueldo = models.FloatField(blank=True, default=None)
	id_cargo = models.ForeignKey(Cargo, null=True, default=None) 
	fe_ingreso = models.DateField(blank=True, default=None)
	fe_egreso = models.DateField(blank=True, default=None)
	status = models.CharField(max_length=1, default="1")
	
	def __unicode__(self):
		return "%s" % (self.ci,self.nb_1,self.ap_1)


class Cliente(models.Model):
	id_cliente = models.AutoField(primary_key=True)
	rif= models.CharField(max_length=10, unique=True)
	nb_cliente = models.CharField(max_length=100)
	dir_cliente = models.TextField()
	tlf1 = models.CharField(max_length=15)
	tlf2 = models.CharField(max_length=15)
	fax = models.CharField(max_length=15)
	mail = models.EmailField(null=True, default=None)
	iva = models.BooleanField(default=False)
	status = models.CharField(max_length=1, default="1")
		
	def __unicode__(self):
		return "%s" % (self.nb_cliente)


class Venta(models.Model):
	id_venta = models.AutoField(primary_key=True)
	cliente = models.ForeignKey(Cliente, blank=True, default=None)
	producto = models.ForeignKey(Producto, blank=True, default=None)
	cantidad = models.IntegerField()
	fe_venta = models.DateField(null=True)
	status = models.CharField(max_length=1, default="1")