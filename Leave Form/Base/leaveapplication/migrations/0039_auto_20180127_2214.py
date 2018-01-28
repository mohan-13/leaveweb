# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-27 16:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapplication', '0038_auto_20180127_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='from_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 27, 22, 14, 12, 476345)),
        ),
        migrations.AlterField(
            model_name='students',
            name='status',
            field=models.CharField(choices=[(1, 'SUBMITTED'), (2, 'APPROVED'), (3, 'DENIED')], default='SUBMITTED', max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='to_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 27, 22, 14, 12, 476345)),
        ),
    ]