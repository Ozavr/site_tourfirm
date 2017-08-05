# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-20 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_mail', '0003_requestlist_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestlist',
            name='description',
            field=models.TextField(blank=True, max_length=768, verbose_name='Краткое содержание вашей заявки'),
        ),
    ]
