# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-18 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0043_request_progress_request_event_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_progress',
            name='request_creater_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='team_approval_progress',
            name='team_creater_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]