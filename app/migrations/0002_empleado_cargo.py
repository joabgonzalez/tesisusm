# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='cargo',
            field=models.ForeignKey(default=None, blank=True, to='app.Cargo', null=True),
            preserve_default=True,
        ),
    ]
