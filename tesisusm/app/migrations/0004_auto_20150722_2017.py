# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_empleado_cargo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Impuesto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='iva',
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_tipo_prod',
            field=models.ForeignKey(default=None, blank=True, to='app.Tipo_Producto', null=True),
            preserve_default=True,
        ),
    ]
