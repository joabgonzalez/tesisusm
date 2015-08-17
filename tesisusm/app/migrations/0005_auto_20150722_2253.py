# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150722_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='status',
            field=models.CharField(default=b'1', max_length=1),
            preserve_default=True,
        ),
    ]
