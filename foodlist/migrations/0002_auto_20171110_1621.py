# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, to='foodlist.Category', verbose_name='\u5206\u7c7b'),
        ),
    ]
