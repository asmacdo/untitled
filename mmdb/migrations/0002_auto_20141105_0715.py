# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='work_type',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='person_birth_date',
            field=models.DateField(verbose_name='birth date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_first_name',
            field=models.CharField(verbose_name='First Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_last_name',
            field=models.CharField(verbose_name='Last Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='rel_name',
            field=models.CharField(verbose_name='Relationship', max_length=100),
        ),
    ]
