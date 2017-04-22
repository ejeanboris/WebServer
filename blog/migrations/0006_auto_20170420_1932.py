# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-20 23:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_mailbox_connected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailbox',
            name='connected',
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.MailBox'),
        ),
    ]
