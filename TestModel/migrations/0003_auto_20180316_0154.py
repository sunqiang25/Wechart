# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-03-16 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_auto_20180316_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qiushi_joke',
            name='comment_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='qiushi_joke',
            name='laugh_num',
            field=models.IntegerField(),
        ),
    ]
