# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView

from .models import OrganizationTree
from person.models import WorkRecord

def show_genres(request):
    nodes = OrganizationTree.objects.all()
    # print(nodes)
    genre = nodes[1]
    return render_to_response("genres.html", locals())




# show_org
def show_org(request):
    nodes = OrganizationTree.objects.all()
    genre = nodes[1]
    return render_to_response("org_list.html", locals(), context_instance=RequestContext(request))

# show_org_person
class ShowOrgPersonsListView(ListView):
    model = WorkRecord
    template_name = 'org_list_person.html'
    # context_object_name = 'person'
    pk_url_kwarg = 'person_id'
    # context_object_name = 'employee'
    # print(context_object_name)
    # paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super(ShowOrgPersonsListView, self).get_context_data(**kwargs)
        nodes = OrganizationTree.objects.all()
        genre = nodes[1]
        context['genre'] = genre
        # context['c'] = context['genre']
        # print(context)
        return context

    def get_queryset(self):
        return WorkRecord.objects.filter(organization=self.kwargs['pk']).order_by('person__id')

