# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-19 06:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0033_auto_20171216_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type1',
            name='year',
        ),
        migrations.RemoveField(
            model_name='type2',
            name='year',
        ),
    ]