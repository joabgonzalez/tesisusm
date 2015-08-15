# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150723_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='status',
            field=models.CharField(default=b'1', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='venta',
            name='status',
            field=models.CharField(default=b'1', max_length=1),
            preserve_default=True,
        ),
    ]
