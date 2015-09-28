# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150928_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='descripcion',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fax',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_2',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rol_usuario',
            name='descripcion',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tipo_empleado',
            name='descripcion',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tipo_producto',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='segundo_apellido',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='segundo_nombre',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ultima_conexion',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='utilidad_mensual',
            name='abr',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='utilidad_mensual',
            name='ago',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='utilidad_mensual',
            name='dic',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='utilidad_mensual',
            name='ene',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='utilidad_mensual',
            name='feb',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='utilidad_mensual',
            name='jul',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='utilidad_mensual',
            name='jun',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='utilidad_mensual',
            name='mar',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='utilidad_mensual',
            name='may',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='utilidad_mensual',
            name='nov',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='utilidad_mensual',
            name='oct',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='utilidad_mensual',
            name='sep',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
