# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmdb', '0004_auto_20141105_0751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='work_parent',
        ),
    ]
