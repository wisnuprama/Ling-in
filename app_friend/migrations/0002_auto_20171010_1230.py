# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_friend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
