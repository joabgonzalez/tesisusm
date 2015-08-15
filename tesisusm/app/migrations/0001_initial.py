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
                ('nb_cargo', models.CharField(max_length=50)),
                ('desc_cargo', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(serialize=False, primary_key=True)),
                ('ci', models.CharField(max_length=50)),
                ('nb_1', models.CharField(max_length=50)),
                ('nb_2', models.CharField(max_length=50)),
                ('ap_1', models.CharField(max_length=50)),
                ('ap_2', models.CharField(max_length=50)),
                ('tlf1', models.CharField(max_length=15)),
                ('cel', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('id_impuesto', models.AutoField(serialize=False, primary_key=True)),
                ('iva', models.FloatField()),
                ('flete', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_prod', models.AutoField(serialize=False, primary_key=True)),
                ('cod_prod', models.CharField(max_length=10)),
                ('nb_prod', models.CharField(max_length=100)),
                ('id_tipo_prod', models.CharField(max_length=10)),
                ('desc_prod', models.TextField()),
                ('precio_prod', models.FloatField()),
                ('status', models.CharField(max_length=1)),
                ('iva', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rol_Usuario',
            fields=[
                ('id_rol', models.AutoField(serialize=False, primary_key=True)),
                ('nb_rol', models.CharField(max_length=50)),
                ('desc_rol', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Producto',
            fields=[
                ('id_tipo_producto', models.AutoField(serialize=False, primary_key=True)),
                ('nb_tipo_producto', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=75)),
                ('fe_create', models.DateTimeField(auto_now_add=True)),
                ('id_rol', models.ForeignKey(default=None, blank=True, to='app.Rol_Usuario', null=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
