# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0019_auto_20170727_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fscjob',
            name='password',
            field=models.CharField(default='0c43ec8d45', max_length=20),
        ),
        migrations.AlterField(
            model_name='fscjob',
            name='uniquefolder',
            field=models.CharField(default='e3fc13c17f71a6b5985b', max_length=20),
        ),
    ]
