# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180530_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
