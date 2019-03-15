# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-15 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='city_name',
        ),
        migrations.RemoveField(
            model_name='location',
            name='country_name',
        ),
        migrations.AddField(
            model_name='location',
            name='photo_location',
            field=models.CharField(default=6, max_length=50),
            preserve_default=False,
        ),
    ]
