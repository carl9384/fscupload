# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-07-25 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20170725_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='halfmap1file',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
