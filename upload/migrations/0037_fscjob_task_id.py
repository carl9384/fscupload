# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-05 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0036_auto_20180304_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='fscjob',
            name='task_id',
            field=models.CharField(default='', max_length=36, null=True, verbose_name='Task ID'),
        ),
    ]
