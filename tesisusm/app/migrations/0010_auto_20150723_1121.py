# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20150722_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(serialize=False, primary_key=True)),
                ('rif', models.CharField(unique=True, max_length=10)),
                ('nb_cliente', models.CharField(max_length=100)),
                ('dir_cliente', models.TextField()),
                ('tlf1', models.CharField(max_length=15)),
                ('tlf2', models.CharField(max_length=15)),
                ('fax', models.CharField(max_length=15)),
                ('mail', models.EmailField(default=None, max_length=75, null=True)),
                ('iva', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(serialize=False, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('fe_venta', models.DateField(null=True)),
                ('cliente', models.ForeignKey(default=None, blank=True, to='app.Cliente')),
                ('producto', models.ForeignKey(default=None, blank=True, to='app.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fe_nac',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='id_cargo',
            field=models.ForeignKey(default=None, to='app.Cargo', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='mail',
            field=models.EmailField(default=None, max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_tipo_prod',
            field=models.ForeignKey(default=None, to='app.Tipo_Producto', null=True),
            preserve_default=True,
        ),
    ]
