from rest_framework import serializers
from imdb_api.models import Movies, Genre


class MoviesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'
        depth = 1


