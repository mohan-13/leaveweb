# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-25 15:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapplication', '0030_auto_20180125_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 25, 21, 21, 5, 335275)),
        ),
    ]