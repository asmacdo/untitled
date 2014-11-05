# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmdb', '0003_auto_20141105_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='work_parent',
            field=models.ForeignKey(to='mmdb.BaseWork', null=True),
        ),
    ]
