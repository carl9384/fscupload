# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0015_fscjob_uniquefolder'),
    ]

    operations = [
        migrations.AddField(
            model_name='fscjob',
            name='password',
            field=models.CharField(default='f9607526a6', max_length=20),
        ),
        migrations.AlterField(
            model_name='fscjob',
            name='uniquefolder',
            field=models.CharField(default='b8d76b0f66d115f77d17', max_length=20),
        ),
    ]
