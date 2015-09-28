# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='correo_corporativo',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_egreso',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='segundo_apellido',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='segundo_nombre',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono_local',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
