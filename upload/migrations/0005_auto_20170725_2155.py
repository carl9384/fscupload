# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_auto_20170725_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='halfmap1file',
            field=models.FileField(upload_to='halfmap1/'),
        ),
    ]
