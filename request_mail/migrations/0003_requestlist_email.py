# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-13 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_mail', '0002_auto_20161121_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlist',
            name='email',
            field=models.CharField(blank=True, max_length=20, verbose_name='email'),
        ),
    ]