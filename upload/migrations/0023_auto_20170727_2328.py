# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0022_auto_20170727_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fscjob',
            name='completefile',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='fscjob',
            name='password',
            field=models.CharField(default='b1ac8b039a', max_length=20),
        ),
        migrations.AlterField(
            model_name='fscjob',
            name='uniquefolder',
            field=models.CharField(default='5227b439a109d59b110c', max_length=20),
        ),
    ]
