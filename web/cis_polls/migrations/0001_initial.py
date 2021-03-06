# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('percent', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('answer_int', models.SmallIntegerField()),
                ('answer_text', models.CharField(max_length=200)),
                ('is_nsnc', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Facet',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
                ('value', models.SmallIntegerField()),
                ('facet_text', models.CharField(max_length=200)),
                ('is_total', models.BooleanField(default=False)),
                ('sample', models.PositiveIntegerField(verbose_name='N')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('kind', models.CharField(unique_for_date='date', max_length=50)),
                ('poll_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('cis_study_id', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
                ('question_text', models.CharField(max_length=200)),
                ('sample', models.PositiveIntegerField(verbose_name='N')),
                ('poll', models.ForeignKey(to='cis_polls.Poll')),
            ],
        ),
        migrations.AddField(
            model_name='facet',
            name='question',
            field=models.ForeignKey(to='cis_polls.Question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='cis_polls.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(to='cis_polls.Choice'),
        ),
        migrations.AddField(
            model_name='answer',
            name='facet',
            field=models.ForeignKey(to='cis_polls.Facet', blank=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='cis_polls.Question'),
        ),
    ]
