# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_posts_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='log_text',
            field=models.CharField(default='No logs available.', max_length=9000),
        ),
    ]
