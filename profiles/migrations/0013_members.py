# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160218135022 on 2016-02-27 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20160227_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(default='http://i.imgur.com/y6nAFKz.jpg', max_length=1024)),
                ('desc_text', models.CharField(default='No description :(', max_length=200)),
            ],
        ),
    ]
