# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.15 on 2018-09-09 19:02
=======
# Generated by Django 1.11.15 on 2018-09-05 14:01
>>>>>>> 58adcb21a03f8a649f125a626dc43b3b0386df35
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
<<<<<<< HEAD
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='main.TypeMultimedia'),
=======
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.TypeMultimedia'),
>>>>>>> 58adcb21a03f8a649f125a626dc43b3b0386df35
            preserve_default=False,
        ),
    ]
