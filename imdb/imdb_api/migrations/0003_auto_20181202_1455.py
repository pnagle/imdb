# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-02 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_api', '0002_movies_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='genre',
        ),
        migrations.AddField(
            model_name='movies',
            name='genre',
            field=models.ManyToManyField(default=None, to='imdb_api.Genre'),
        ),
    ]
