# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacemap', '0004_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='color',
            field=models.CharField(default='#FFFFFF', max_length=8),
        ),
    ]