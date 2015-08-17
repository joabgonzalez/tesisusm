# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_empleado_fe_nac'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='direccion',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='fe_egreso',
            field=models.DateField(default=None, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='fe_ingreso',
            field=models.DateField(default=None, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='id_cargo',
            field=models.ForeignKey(default=None, blank=True, to='app.Cargo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='mail',
            field=models.EmailField(default=None, max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='status',
            field=models.CharField(default=b'1', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='sueldo',
            field=models.FloatField(default=None, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='ci',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fe_nac',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
    ]
