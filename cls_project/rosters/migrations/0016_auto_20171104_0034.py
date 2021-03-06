# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0015_auto_20171104_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(blank=True, choices=[('Attack', 'Attack'), ('Defense', 'Defense'), ('Goalie', 'Goalie'), ('Midfield', 'Midfield'), ('Long Stick Midfield', 'Long Stick Midfield'), ('Attack/Midfield', 'Attack/Midfield'), ('FaceOff', 'FaceOff')], default='fr', help_text='Player Position', max_length=30),
        ),
    ]
