# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmdb', '0005_remove_work_work_parent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BaseWork',
        ),
    ]
