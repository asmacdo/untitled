# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmdb', '0006_delete_basework'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='work_parent',
            field=models.ForeignKey(null=True, to='mmdb.Work'),
            preserve_default=True,
        ),
    ]
