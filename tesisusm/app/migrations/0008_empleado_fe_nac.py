# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150722_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='fe_nac',
            field=models.DateField(default=None),
            preserve_default=True,
        ),
    ]
