# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-04 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('email_id', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
