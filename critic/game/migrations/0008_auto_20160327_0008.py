# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_movie_poster_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='similar',
            name='real',
            field=models.CharField(default='none', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='similar',
            name='real_u',
            field=models.CharField(default='none', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='similar',
            name='url1',
            field=models.CharField(default='none', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='similar',
            name='url2',
            field=models.CharField(default='none', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='similar',
            name='url3',
            field=models.CharField(default='none', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='similar',
            name='url4',
            field=models.CharField(default='none', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='similar',
            name='url5',
            field=models.CharField(default='none', max_length=150),
            preserve_default=False,
        ),
    ]