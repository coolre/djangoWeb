# -*- coding: utf-8 -*-

from .models import OrganizationTree
from django.shortcuts import render_to_response
from django.template import RequestContext

def show_genres(request):
    nodes = OrganizationTree.objects.all()
    genre = nodes[1]
    return render_to_response("genres.html", locals())

