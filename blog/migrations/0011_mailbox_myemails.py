# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-13 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170420_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailbox',
            name='myEmails',
            field=models.TextField(default='Begin'),
        ),
    ]