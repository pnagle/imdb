# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from imdb_api.models import Movies, Genre
# Register your models here.


admin.site.register(Movies)
admin.site.register(Genre)
