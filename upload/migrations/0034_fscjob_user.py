# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 20:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload', '0033_auto_20170804_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='fscjob',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
