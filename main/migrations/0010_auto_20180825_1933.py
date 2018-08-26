# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-25 19:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20180819_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='file',
            name='url',
            field=models.CharField(max_length=300),
        ),
    ]
