# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_auto_20160416_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='type',
            field=models.CharField(choices=[('megastation', 'megastation'), ('intercitystation', 'intercitystation'), ('knooppuntIntercitystation', 'knooppuntIntercitystation'), ('sneltreinstation', 'sneltreinstation'), ('knooppuntSneltreinstation', 'knooppuntSneltreinstation'), ('stoptreinstation', 'stoptreinstation'), ('knooppuntStoptreinstation', 'knooppuntStoptreinstation'), ('facultatiefStation', 'facultatiefStation')], default='stoptreinstation', max_length=100),
        ),
    ]