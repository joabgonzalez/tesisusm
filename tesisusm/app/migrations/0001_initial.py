# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta_Usuario',
            fields=[
                ('id_pregunta', models.AutoField(serialize=False, primary_key=True)),
                ('nb_pregunta', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rol_Usuario',
            fields=[
                ('id_rol', models.AutoField(serialize=False, primary_key=True)),
                ('nb_rol', models.CharField(max_length=50)),
                ('desc_rol', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.AutoField(serialize=False, primary_key=True)),
                ('user', models.CharField(max_length=20)),
                ('clave', models.CharField(max_length=20)),
                ('nb_usuario', models.CharField(max_length=50)),
                ('ap_usuario', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('nb_respuesta', models.CharField(max_length=50)),
                ('fe_create', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('id_pregunta', models.ForeignKey(to='app.Pregunta_Usuario')),
                ('id_rol', models.ForeignKey(default=None, blank=True, to='app.Rol_Usuario', null=True)),
            ],
        ),
    ]
