# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-21 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0047_team_detail_creator_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_progress',
            name='rejection_reason',
            field=models.CharField(default='', max_length=400),
        ),
    ]