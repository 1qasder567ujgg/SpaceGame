# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spacemap', '0003_planet'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inhabited', models.BooleanField(default=False)),
                ('shop', models.BooleanField(default=False)),
                ('garage', models.BooleanField(default=False)),
                ('space_port', models.BooleanField(default=False)),
                ('population', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('city_status', models.CharField(choices=[('Village', 'Village'), ('Town', 'Town'), ('City', 'City')], default='Village', max_length=10)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spacemap.Planet')),
            ],
        ),
    ]
