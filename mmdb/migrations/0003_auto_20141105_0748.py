# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmdb', '0002_auto_20141105_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='work',
            name='work_parent',
            field=models.ForeignKey(default='', to='mmdb.BaseWork'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='work',
            name='work_name',
            field=models.CharField(verbose_name='Work Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='work',
            name='work_type',
            field=models.CharField(verbose_name='Work Type', max_length=100),
        ),
    ]
