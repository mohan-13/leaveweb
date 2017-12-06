# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='reason',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
