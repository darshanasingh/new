# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0003_auto_20180628_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmer',
            name='languages',
            field=models.ManyToManyField(to='languages.Language'),
        ),
    ]
