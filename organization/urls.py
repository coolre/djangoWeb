# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import show_genres

urlpatterns = [
    url(r'^$', show_genres, name="show_genres"),
]