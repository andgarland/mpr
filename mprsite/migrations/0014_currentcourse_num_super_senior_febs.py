# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-16 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mprsite', '0013_auto_20161215_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentcourse',
            name='num_super_senior_febs',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]