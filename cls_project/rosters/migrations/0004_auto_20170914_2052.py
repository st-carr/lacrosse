# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0003_auto_20170914_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('d1', 'Division 1'), ('d2', 'Division 2'), ('d3', 'Division 3')], default='d1', help_text='NCAA Division', max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='division',
        ),
        migrations.RemoveField(
            model_name='player',
            name='league',
        ),
        migrations.AddField(
            model_name='school',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rosters.League'),
        ),
        migrations.AddField(
            model_name='league',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rosters.Division'),
        ),
    ]
