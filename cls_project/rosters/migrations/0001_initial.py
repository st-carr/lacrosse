# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(blank=True, choices=[('d1', 'Division 1'), ('d2', 'Division 2'), ('d3', 'Division 3')], default='d1', help_text='NCAA Division', max_length=2)),
                ('height', models.PositiveSmallIntegerField()),
                ('league', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('number', models.PositiveSmallIntegerField()),
                ('position', models.CharField(blank=True, choices=[('atk', 'Attack'), ('def', 'Defense'), ('gl', 'Goalie'), ('mid', 'Midfield'), ('lsm', 'Long Stick Midfield'), ('am', 'Attack/Midfield'), ('fo', 'FaceOff')], default='fr', help_text='Player Position', max_length=3)),
                ('school', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('weight', models.PositiveSmallIntegerField()),
                ('year', models.CharField(blank=True, choices=[('rs', 'RedShirt'), ('fr', 'Freshman'), ('so', 'Sophomore'), ('jr', 'Junior'), ('sr', 'Senior'), ('gr', 'Graduate')], default='fr', help_text='Player Class Standing', max_length=2)),
                ('city', models.CharField(max_length=200)),
                ('high_school', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['school', 'number'],
            },
        ),
    ]
