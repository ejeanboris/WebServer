# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-21 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170420_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(),
        ),
    ]
