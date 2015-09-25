# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='cantidad',
            new_name='cantidad_producto',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='producto',
            new_name='producto_producto',
        ),
        migrations.AddField(
            model_name='inventario',
            name='codigo_producto',
            field=models.CharField(default='', unique=True, max_length=10),
            preserve_default=False,
        ),
    ]
