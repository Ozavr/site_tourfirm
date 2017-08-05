# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-10 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestSpb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.CharField(blank=True, max_length=20, verbose_name='email')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Список запросов в spb',
                'verbose_name_plural': 'Список запросов в spb',
                'ordering': ['-date'],
            },
        ),
    ]
