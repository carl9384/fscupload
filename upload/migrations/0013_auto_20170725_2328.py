# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-07-25 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0012_auto_20170725_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fscjob',
            name='apix',
            field=models.FloatField(default=1.1),
        ),
    ]
