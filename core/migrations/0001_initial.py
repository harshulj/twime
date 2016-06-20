# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 21:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256)),
                ('username', models.CharField(max_length=256)),
                ('url', models.URLField(blank=True, max_length=128)),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('verified', models.BooleanField(default=False)),
                ('tweet_count', models.PositiveIntegerField(default=0)),
                ('time_zone', models.CharField(blank=True, max_length=128)),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('language', models.CharField(blank=True, max_length=16)),
                ('followers_count', models.PositiveIntegerField(default=0)),
                ('following_count', models.PositiveIntegerField(default=0)),
                ('listed_count', models.PositiveIntegerField(default=0)),
                ('favourites_count', models.PositiveIntegerField(default=0)),
                ('profile_image_url', models.URLField(blank=True)),
                ('raw', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={})),
                ('account_created_on', models.DateTimeField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('best_time', models.TimeField(blank=True, null=True)),
                ('best_day', models.CharField(blank=True, choices=[(b'sun', b'Sunday'), (b'mon', b'Monday'), (b'tue', b'Tuesday'), (b'wed', b'Wednesday'), (b'thu', b'Thrusday'), (b'fri', b'Friday'), (b'sat', b'Saturday')], max_length=3, null=True)),
            ],
        ),
    ]
