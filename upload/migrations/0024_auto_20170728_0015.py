# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0023_auto_20170727_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fscjob',
            name='password',
            field=models.CharField(default='9ba8ae4278', max_length=20),
        ),
        migrations.AlterField(
            model_name='fscjob',
            name='uniquefolder',
            field=models.CharField(default='093111402c7bd6416d87', max_length=20),
        ),
    ]
