# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_auto_20170725_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='apix',
            field=models.FloatField(default=19),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='coneangle',
            field=models.FloatField(default=20),
        ),
        migrations.AddField(
            model_name='document',
            name='fsccutoff',
            field=models.FloatField(default=0.143),
        ),
        migrations.AddField(
            model_name='document',
            name='fullmapfile',
            field=models.FileField(default=10, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='halfmap2file',
            field=models.FileField(default=10, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='highpassilfter',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='document',
            name='maskfile',
            field=models.FileField(default=10, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='sphericitythresh',
            field=models.FloatField(default=0.5),
        ),
    ]
