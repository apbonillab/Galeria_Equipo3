# -*- coding: utf-8 -*-

# Generated by Django 1.11.15 on 2018-09-05 14:01

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20180826_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.TypeMultimedia'),
            preserve_default=False,
        ),
    ]
