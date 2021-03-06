# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('type', models.CharField(choices=[('MEG', 'megastation'), ('IC', 'intercitystation'), ('ICK', 'knooppuntIntercitystation'), ('SNT', 'sneltreinstation'), ('SNK', 'knooppuntSneltreinstation'), ('STK', 'knooppuntStoptreinstation'), ('ST', 'stoptreinstation'), ('FAC', 'facultatiefStation')], default='ST', max_length=3)),
                ('name_long', models.CharField(max_length=200)),
                ('name_middle', models.CharField(max_length=150)),
                ('name_short', models.CharField(max_length=100)),
            ],
        ),
    ]
