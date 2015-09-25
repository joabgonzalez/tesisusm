# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150922_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='producto_producto',
            new_name='nombre_producto',
        ),
    ]
