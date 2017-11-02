# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.db.models import Count
from django.utils import timezone

from .models import OrganizationTree
from person.models import WorkRecord, Certificate, Person

def show_genres(request):
    nodes = OrganizationTree.objects.all()
    # print(nodes)
    genre = nodes[1]
    return render_to_response("genres.html", locals())

#
# # show_org
# def show_org(request):
#     nodes = OrganizationTree.objects.all()
#     genre = nodes[1]
#     print(genre)
#     return render_to_response("org_list.html", locals(), context_instance=RequestContext(request))
#
# # show_org_person
# class ShowOrgPersonsListView(ListView):
#     # model = WorkRecord
#     # queryset = WorkRecord.objects.exclude(part_time='t')
#     template_name = 'org_list_person.html'
#     # context_object_name = 'person'
#     pk_url_kwarg = 'person_id'
#     # context_object_name = 'employee'
#
#
#
#     def get_context_data(self, **kwargs):
#         context = super(ShowOrgPersonsListView, self).get_context_data(**kwargs)
#         nodes = OrganizationTree.objects.all()
#         genre = nodes[1]
#         # print(genre)
#         context['genre'] = genre
#         # certificate = Certificate.objects.values_list('name', flat=True)
#         # context['certificate'] = certificate
#         # print(context)
#         return context
#
#     def get_queryset(self):
#         workrecord_list = WorkRecord.objects.filter(organization=self.kwargs['pk']).order_by('part_time', '-department__order_num', '-post__order_num', 'person__id')
#         for workrecord in workrecord_list:
#             person = workrecord.person
#             certificate = Certificate.objects.filter(person=person).values_list("name", flat=True).distinct()
#             workrecord.certificate = list(certificate)
#             workrecord.age = Person.get_age(person)
#
#
#         person_list = workrecord_list.values_list("person", flat=True)
#         workrecord.num = len(list(set(person_list)))
#
#
#         return workrecord_list

           # .exclude(part_time='t')
        # print(workrecord_list)

        # return queryset

