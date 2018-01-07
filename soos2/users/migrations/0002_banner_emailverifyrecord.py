# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 14:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图')),
                ('url', models.URLField(verbose_name='访问地址')),
                ('index', models.ImageField(default=100, upload_to='', verbose_name='顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2018, 1, 7, 14, 56, 55, 168435, tzinfo=utc), verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '轮播图',
                'verbose_name': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='EmailverifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '找回密码')], max_length=10)),
                ('send_time', models.DateTimeField(default=datetime.datetime(2018, 1, 7, 14, 56, 55, 167676, tzinfo=utc))),
            ],
            options={
                'verbose_name_plural': '邮箱验证',
                'verbose_name': '邮箱验证',
            },
        ),
    ]
