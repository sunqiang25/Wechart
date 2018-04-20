# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-03-16 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='qiushi_joke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=1024)),
                ('laugh_num', models.IntegerField(max_length=11)),
                ('comment_num', models.IntegerField(max_length=11)),
                ('imgurl', models.CharField(max_length=256)),
            ],
        ),
    ]
