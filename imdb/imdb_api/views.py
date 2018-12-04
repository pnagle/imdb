# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from imdb_api.serializers import MoviesSerializers
from .models import Movies, Genre
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response

# Create your views here.


class MoviesViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited movies.
    """
    # queryset = Movies.objects.all().order_by('-popularity')
    serializer_class = MoviesSerializers
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class movies_list(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all Movies
    """
    # queryset = Movies.objects.all()
    serializer_class = MoviesSerializers
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        orderby = self.request.query_params.get('orderby', None)
        if orderby:
            queryset = Movies.objects.all().order_by('-'+orderby+'')
        else:
            queryset = Movies.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class movies_detail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a movie.
    """
    # queryset = Movies.objects.all()
    serializer_class = MoviesSerializers

    def get_queryset(self):
        queryset = Movies.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(movies__name=name).order_by('-popularity')
        return queryset

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



