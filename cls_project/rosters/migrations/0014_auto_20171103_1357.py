# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0013_auto_20171103_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['school', 'number'], 'permissions': (('can_edit_player', 'Can edit player'),)},
        ),
    ]
