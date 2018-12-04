# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Movies(models.Model):
    name = models.CharField(max_length=128)
    imdb_score = models.FloatField()
    director = models.CharField(max_length=128)
    popularity = models.FloatField()
    genre = models.ManyToManyField('Genre', default=None)

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return str(self.name)


class Genre(models.Model):
    genre_name = models.CharField(max_length=128)

    def __unicode__(self):
        return '%s' % self.genre_name

    def __str__(self):
        return str(self.genre_name)
