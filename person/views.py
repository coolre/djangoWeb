# coding: utf-8
from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from django_tables2 import RequestConfig
from pyecharts import Bar

from djangoWeb.echarts import EchartsView
from organization.models import OrganizationTree

from .models import Person, Contact, Contract, WorkRecord, Certificate, CertificateRecod, CertificatePhoto, Salary, CertificatesType
from .tables import ContactTable, ContractTable, WorkrecordTable, CertificateTable

# index page
def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': 23}
    return render(request, 'home.html', context)


# show_org_person
class ShowOrgPersonsListView(ListView):
    # model = WorkRecord
    # queryset = WorkRecord.objects.exclude(part_time='t')
    template_name = 'org_list_person.html'
    # context_object_name = 'person'
    pk_url_kwarg = 'person_id'

    def get_context_data(self, **kwargs):
        context = super(ShowOrgPersonsListView, self).get_context_data(**kwargs)
        nodes = OrganizationTree.objects.all()
        genre = nodes[1]
        # print(genre)
        context['genre'] = genre
        # certificate = certificate.objects.values_list('name', flat=True)
        # context['certificate'] = certificate
        # print(context)
        return context

    def get_queryset(self):
        workrecord_list = WorkRecord.objects.filter(organization=self.kwargs['pk']).order_by('part_time',
                                                                                             '-department__order_num',
                                                                                             '-post__order_num',
                                                                                             'person__id')
        for workrecord in workrecord_list:
            person = workrecord.person
            certificate = Certificate.objects.filter(person=person).values_list("name__type_name", flat=True).distinct()
            workrecord.certificate = list(certificate)
            workrecord.age = Person.get_age(person)
            workrecord.mobile= Person.get_person_mobile(person)

        person_list = workrecord_list.values_list("person", flat=True)
        workrecord.num = len(list(set(person_list)))
        return workrecord_list

# show_org_personcontact
class ShowOrgPersonscontactListView(ListView):
    # model = WorkRecord
    # queryset = WorkRecord.objects.exclude(part_time='t')
    template_name = 'org_list_contact.html'
    # context_object_name = 'person'
    pk_url_kwarg = 'person_id'

    def get_context_data(self, **kwargs):
        context = super(ShowOrgPersonscontactListView, self).get_context_data(**kwargs)
        # nodes = OrganizationTree.objects.all()
        # genre = nodes[1]
        # # print(genre)
        # context['genre'] = genre
        return context

    def get_queryset(self):
        list = WorkRecord.objects.filter(organization=self.kwargs['pk']).order_by('part_time',
                                                                                             '-department__order_num',
                                                                                             '-post__order_num',
                                                                                             'person__id')
        for workrecord in list:
            person = workrecord.person
            # contact = Contact.objects.filter(person=person)
            # print(contact)
            # workrecord.certificate = list(contact)
            workrecord.age = Person.get_age(person)
            workrecord.mobile = Person.get_person_mobile(person)

        return list




from django.shortcuts import get_object_or_404


class TypeCertificateList(ListView):
    model = Certificate
    template_name = 'certificate/certificates_by_type.html'
    pk_url_kwarg = 'CertificatesType_id'

    def get_queryset(self):
        self.name = get_object_or_404(CertificatesType, id=self.kwargs['CertificatesType_id'])
        list = Certificate.objects.filter(name__type_name=self.name)
        return list

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(TypeCertificateList, self).get_context_data(**kwargs)
    #     # Add in the publisher
    #     context['num'] = self.name
    #     return context


# Person_Detail
class PersonDetailView(DetailView):
    model = Person
    template_name = 'person_detail.html'
    context_object_name = 'person'
    pk_url_kwarg = 'person_id'

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['contact_list'] = Contact.objects.filter(person_id=self.kwargs['person_id'])
        context['workrecord_list'] = WorkRecord.objects.filter(person_id=self.kwargs['person_id'])
        context['certificate_list'] = Certificate.objects.filter(person_id=self.kwargs['person_id'])
        return context


def contact(request):
    table = ContactTable(Contact.objects.all(), order_by='id')
    RequestConfig(request, paginate={'per_page': 40}).configure(table)
    return render(request, 'person_contact.html', {'Contact': table})

def contract(request):
    table = ContractTable(Contract.objects.all(), order_by='id')
    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    return render(request, 'person_contract.html', {'Contract': table})

def workrecord(request):
    table = WorkrecordTable(WorkRecord.objects.all(), order_by='id')
    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    return render(request, 'person_workrecord.html', {'Workrecord': table})

def certificate(request):
    table = CertificateTable(Certificate.objects.all(), order_by='id')
    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    return render(request, 'person_certificate.html', {'certificate': table})

class CertificateDetailView(DetailView):
    model = Certificate
    template_name = 'certificate_detail.html'
    context_object_name = 'certificate'
    pk_url_kwarg = 'Certificate_id'

    def get_context_data(self, **kwargs):
        context = super(CertificateDetailView, self).get_context_data(**kwargs)
        context['certificate_record_list'] = CertificateRecod.objects.filter(certificate_id=self.kwargs['Certificate_id'])
        context['certificate_photo'] = CertificatePhoto.objects.filter(certificate_id=self.kwargs['Certificate_id'])
        # context['certificate_list'] = certificate.objects.filter(person_id=self.kwargs['person_id'])
        # print(context)
        return context










# #charjs#


from collections import defaultdict
from django.http import HttpResponse
from django.template import loader

class SalaryChartsView(TemplateView):
    template_name = 'Salary_charts.html'


def money_sum(data):
    c = defaultdict(float)
    for d in data:
        c[d['person__name']] += d['pay_money']
    return c
# #


def get_year_data(year):
    kwargs = {'belong_year': year,
              'state': 0}
    # kwargs['belong_year'] = year
    data = Salary.objects.values('person__name', 'pay_money', ).filter(**kwargs)
    data = money_sum(data)
    return dict(data)

#
def get_v_data(year):
    attr = get_echarts_option_attr(2016)
    # print(attr)

    data = get_year_data(year)

    v = [([0] * 2) for y in range(len(attr))]
    # print(v)

    year_data = []

    for i in range(0, len(attr)):
        v[i][0] = attr[i]
        k = v[i][0]

        if k in data.keys():
            v[i][1] = data.get(k)
        else:
            v[i][1] = data.get(k, 0)
        year_data.append(v[i][1])

    return year_data


def get_echarts_option_attr(year):
    d = get_year_data(year)
    data = dict(sorted(d.items(), key=lambda d: d[1], reverse=False))
    attr = list(data.keys())
    return attr


class SalaryBarView(EchartsView):

    def get_echarts_option(self, **kwargs):
        attr = get_echarts_option_attr(2016)
        #
        # print(attr)

        v1 = get_v_data(2016)
        v2 = get_v_data(2015)
        v3 = get_v_data(2014)

        bar = Bar("Bar chart", "precipitation and evaporation one year")
        bar.add("2016", attr, v1, mark_line=["average"], mark_point=["max"], yaxis_interval=0,)
        bar.add("2015", attr, v2, mark_line=["average"], mark_point=["max"])
        bar.add("2014", attr, v3, mark_line=["average"], mark_point=["max"],
                xaxis_rotate=90, is_convert=True, interval=0)

        print(bar._option)

        return bar._option

def charts(request):
    template = loader.get_template('charts.html')
    l3d = line3d()
    context = dict(
        myechart=l3d.render_embed(),
        host="http://echarts.baidu.com/dist",
        script_list=l3d.get_js_dependencies(),
    )

    return HttpResponse(template.render(context, request))


def line3d():
    from pyecharts import Bar

    attr = get_echarts_option_attr(2016)
    #
    # print(attr)

    v1 = get_v_data(2016)
    v2 = get_v_data(2015)
    v3 = get_v_data(2014)

    bar = Bar("Bar chart", "precipitation and evaporation one year", width=1300, height=2800)
    bar.add("2016", attr, v1, mark_line=["average"], mark_point=["max"])
    bar.add("2015", attr, v2, mark_line=["average"], mark_point=["max"])
    bar.add("2014", attr, v3, mark_line=["average"], mark_point=["max"],
            is_convert=True, yaxis_interval=0, )

    # print(bar._option)

    return bar