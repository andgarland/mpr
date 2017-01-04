# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mprsite', '0003_auto_20161204_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentcourse',
            name='filled_waitlist_seats',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='currentcourse',
            name='filled_xlist_seats',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pastcourse',
            name='filled_waitlist_seats',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pastcourse',
            name='filled_xlist_seats',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pastcourse',
            name='filled_num_seats',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pastcourse',
            name='max_num_seats',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pastcourse',
            name='waitlist_seats',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pastcourse',
            name='xlist_seats',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pastcourse',
            name='year',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]