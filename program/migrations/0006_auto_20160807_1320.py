# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-07 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0005_auto_20160807_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]