# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20161109_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='ean',
            field=models.CharField(max_length=13),
        ),
    ]