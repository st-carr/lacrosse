# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0009_school_roster_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='school',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='school',
            name='roster_website',
            field=models.URLField(default=''),
        ),
    ]
