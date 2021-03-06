# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0002_league_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rosters.League'),
        ),
        migrations.AlterField(
            model_name='player',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rosters.School'),
        ),
    ]
