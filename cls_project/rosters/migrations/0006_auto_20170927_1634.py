# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0005_player_hs_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='hs_type',
            field=models.CharField(blank=True, choices=[('private', 'Private'), ('public', 'Public')], default='fr', help_text='Private or Public High School', max_length=10),
        ),
    ]
