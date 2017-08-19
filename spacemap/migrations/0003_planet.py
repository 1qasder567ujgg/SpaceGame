# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spacemap', '0002_starsystem_pos_y'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inhabited', models.BooleanField(default=False)),
                ('atmosphere', models.BooleanField(default=False)),
                ('distance', models.FloatField()),
                ('diameter', models.FloatField()),
                ('name', models.CharField(max_length=50)),
                ('star_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spacemap.StarSystem')),
            ],
        ),
    ]