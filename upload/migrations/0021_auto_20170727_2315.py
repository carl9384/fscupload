# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0020_auto_20170727_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='fscjob',
            name='jobname',
            field=models.CharField(default='temp', max_length=15),
        ),
        migrations.AlterField(
            model_name='fscjob',
            name='password',
            field=models.CharField(default='e8d15be20d', max_length=20),
        ),
        migrations.AlterField(
            model_name='fscjob',
            name='uniquefolder',
            field=models.CharField(default='3caa3cf93dd641bbce68', max_length=20),
        ),
    ]
