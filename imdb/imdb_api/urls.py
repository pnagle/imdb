from django.conf.urls import url
from imdb_api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^movies/$', views.movies_list.as_view()),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.movies_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
