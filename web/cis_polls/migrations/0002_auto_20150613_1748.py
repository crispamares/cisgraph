# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cis_polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='facet',
            field=models.ForeignKey(blank=True, to='cis_polls.Facet', null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='percent',
            field=models.FloatField(),
        ),
    ]
