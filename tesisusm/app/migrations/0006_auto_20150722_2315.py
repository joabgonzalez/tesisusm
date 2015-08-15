# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150722_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_prod',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
