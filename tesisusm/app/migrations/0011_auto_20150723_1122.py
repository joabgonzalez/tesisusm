# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150723_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='iva',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
