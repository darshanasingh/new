# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-04 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0008_auto_20180704_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmer',
            name='languages',
            field=models.ManyToManyField(to='languages.Language'),
        ),
    ]