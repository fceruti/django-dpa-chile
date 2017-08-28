# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpa_chile', '0002_comuna_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comuna',
            name='id',
        ),
        migrations.RemoveField(
            model_name='provincia',
            name='id',
        ),
        migrations.RemoveField(
            model_name='region',
            name='id',
        ),
        migrations.AlterField(
            model_name='comuna',
            name='codigo',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='codigo',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='codigo',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
