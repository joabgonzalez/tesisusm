# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150922_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='precio_unitario',
            new_name='precio_producto',
        ),
    ]
