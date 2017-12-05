# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20171120_2108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_time'], 'verbose_name': '\u8bc4\u8bba', 'verbose_name_plural': '\u8bc4\u8bba'},
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(1, '\u6b63\u5e38'), (2, '\u5220\u9664')], default=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.CharField(max_length=256, verbose_name='\u8bc4\u8bba\u76ee\u6807'),
        ),
    ]
