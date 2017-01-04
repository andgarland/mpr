# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mprsite', '0008_remove_pastcourse_reserved_seats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentcourse',
            old_name='days',
            new_name='days_one',
        ),
        migrations.RenameField(
            model_name='currentcourse',
            old_name='end_time',
            new_name='end_time_one',
        ),
        migrations.RenameField(
            model_name='currentcourse',
            old_name='location',
            new_name='location_one',
        ),
        migrations.RenameField(
            model_name='currentcourse',
            old_name='start_time',
            new_name='start_time_one',
        ),
        migrations.AddField(
            model_name='currentcourse',
            name='days_two',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currentcourse',
            name='end_time_two',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AddField(
            model_name='currentcourse',
            name='location_two',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currentcourse',
            name='num_tokens',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='currentcourse',
            name='start_time_two',
            field=models.TimeField(default='00:00'),
        ),
    ]
