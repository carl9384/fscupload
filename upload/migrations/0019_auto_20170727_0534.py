# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0018_auto_20170727_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fscjob',
            name='password',
            field=models.CharField(default='1798025533', max_length=20),
        ),
        migrations.AlterField(
            model_name='fscjob',
            name='uniquefolder',
            field=models.CharField(default='d005da864806e4c568d3', max_length=20),
        ),
    ]
