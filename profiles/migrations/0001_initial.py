# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160218135022 on 2016-02-19 23:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_github', models.CharField(max_length=24)),
                ('upvotes', models.IntegerField(default=0)),
                ('github', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Name')),
            ],
        ),
    ]
