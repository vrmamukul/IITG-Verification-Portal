# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-16 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0055_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='record_team_progress',
            name='stage4',
            field=models.CharField(default='none', max_length=200),
        ),
    ]