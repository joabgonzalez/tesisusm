# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id_cargo', models.AutoField(serialize=False, primary_key=True)),
                ('cargo', models.CharField(unique=True, max_length=50)),
                ('descripcion', models.CharField(default=None, max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(serialize=False, primary_key=True)),
                ('rif', models.CharField(unique=True, max_length=10)),
                ('cliente', models.CharField(max_length=100)),
                ('direccion', models.TextField(max_length=150)),
                ('telefono_1', models.CharField(max_length=15)),
                ('telefono_2', models.CharField(default=None, max_length=15, null=True, blank=True)),
                ('fax', models.CharField(default=None, max_length=15, null=True, blank=True)),
                ('correo', models.EmailField(default=None, max_length=254, null=True, blank=True)),
                ('iva', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(serialize=False, primary_key=True)),
                ('cedula', models.CharField(unique=True, max_length=10)),
                ('primer_nombre', models.CharField(max_length=50)),
                ('segundo_nombre', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('telefono_local', models.CharField(default=None, max_length=15, null=True, blank=True)),
                ('telefono_celular', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField(default=None, null=True, blank=True)),
                ('direccion', models.TextField(max_length=150)),
                ('correo_corporativo', models.EmailField(default=None, max_length=254, null=True, blank=True)),
                ('correo_personal', models.EmailField(max_length=254)),
                ('sueldo', models.DecimalField(max_digits=12, decimal_places=2)),
                ('fecha_ingreso', models.DateField()),
                ('fecha_egreso', models.DateField(default=None, null=True, blank=True)),
                ('cargo', models.ForeignKey(to='app.Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(serialize=False, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=10)),
                ('producto', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField(default=None, null=True, blank=True)),
                ('precio_unitario', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Rol_Usuario',
            fields=[
                ('id_rol', models.AutoField(serialize=False, primary_key=True)),
                ('rol', models.CharField(unique=True, max_length=50)),
                ('descripcion', models.CharField(default=None, max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id_stock', models.AutoField(serialize=False, primary_key=True)),
                ('producto_id', models.IntegerField()),
                ('codigo_producto', models.CharField(unique=True, max_length=10)),
                ('nombre_producto', models.CharField(unique=True, max_length=100)),
                ('cantidad_producto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Empleado',
            fields=[
                ('id_tipo_empleado', models.AutoField(serialize=False, primary_key=True)),
                ('tipo_empleado', models.CharField(max_length=50)),
                ('descripcion', models.CharField(default=None, max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Producto',
            fields=[
                ('id_tipo_producto', models.AutoField(serialize=False, primary_key=True)),
                ('tipo_producto', models.CharField(unique=True, max_length=50)),
                ('descripcion', models.TextField(default=None, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(serialize=False, primary_key=True)),
                ('primer_nombre', models.CharField(max_length=50)),
                ('segundo_nombre', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('correo', models.EmailField(max_length=254)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('ultima_conexion', models.DateTimeField(default=None, null=True, blank=True)),
                ('rol', models.ForeignKey(to='app.Rol_Usuario')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Utilidad_Mensual',
            fields=[
                ('id_utilidad_mensual', models.AutoField(serialize=False, primary_key=True)),
                ('ano', models.IntegerField(unique=True)),
                ('ene', models.IntegerField(default=None, null=True, blank=True)),
                ('feb', models.IntegerField(default=None, null=True, blank=True)),
                ('mar', models.IntegerField(default=None, null=True, blank=True)),
                ('abr', models.IntegerField(default=None, null=True, blank=True)),
                ('may', models.IntegerField(default=None, null=True, blank=True)),
                ('jun', models.IntegerField(default=None, null=True, blank=True)),
                ('jul', models.IntegerField(default=None, null=True, blank=True)),
                ('ago', models.IntegerField(default=None, null=True, blank=True)),
                ('sep', models.IntegerField(default=None, null=True, blank=True)),
                ('oct', models.IntegerField(default=None, null=True, blank=True)),
                ('nov', models.IntegerField(default=None, null=True, blank=True)),
                ('dic', models.IntegerField(default=None, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(serialize=False, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('total_venta', models.DecimalField(max_digits=12, decimal_places=2)),
                ('fecha_venta', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(to='app.Cliente')),
                ('producto', models.ForeignKey(to='app.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(to='app.Tipo_Producto'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='tipo_empleado',
            field=models.ForeignKey(to='app.Tipo_Empleado'),
        ),
    ]
