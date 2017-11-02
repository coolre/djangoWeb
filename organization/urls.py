# -*- coding: utf-8 -*-

from django.conf.urls import url

from django.conf.urls import include, url
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import OrganizationTree
# from .views import ShowOrgPersonsListView


from .views import show_genres

app_name = 'organization'
urlpatterns = [
    url(r'^$', show_genres, name="show_genres"),

]