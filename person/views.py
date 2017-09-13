# coding: utf-8
from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.http import HttpResponse

from django.core import serializers

from django_tables2 import RequestConfig
from pyecharts import Bar

from djangoWeb.echarts import EchartsView
from .models import Person, Contact, Contract, Workrecord, Certificate, CertificateRecod, CertificatePhoto, Salary
from .tables import ContactTable, ContractTable, WorkrecordTable, CertificateTable


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': 23}
    return render(request, 'home.html', context)



class PersonListView(ListView):
     model = Person
     template_name = 'person_list.html'
     context_object_name = 'persons'
     paginate_by = 30


class PersonDetailView(DetailView):
    model = Person
    template_name = 'person_detail.html'
    context_object_name = 'person'
    pk_url_kwarg = 'person_id'
    #
    # def get_certificate_recod(self, **kwargs):
    #     certificate = Certificate.objects.filter(person_id=self.kwargs['person_id'])
    #     certificate_recod = CertificateRecod.objects.filter(paper_id=self.kwargs['person_id'])
    #     return certificate_recod

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['contact_list'] = Contact.objects.filter(person_id=self.kwargs['person_id'])
        context['workrecord_list'] = Workrecord.objects.filter(person_id=self.kwargs['person_id'])
        context['certificate_list'] = Certificate.objects.filter(person_id=self.kwargs['person_id'])
        # print(context)
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
    table = WorkrecordTable(Workrecord.objects.all(), order_by='id')
    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    return render(request, 'person_workrecord.html', {'Workrecord': table})


def certificate(request):
    table = CertificateTable(Certificate.objects.all(), order_by='id')
    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    return render(request, 'person_certificate.html', {'Certificate': table})

class CertificateDetailView(DetailView):
    model = Certificate
    template_name = 'certificate_detail.html'
    context_object_name = 'Certificate'
    pk_url_kwarg = 'Certificate_id'

    def get_context_data(self, **kwargs):
        context = super(CertificateDetailView, self).get_context_data(**kwargs)
        context['certificate_record_list'] = CertificateRecod.objects.filter(paper_id=self.kwargs['Certificate_id'])
        context['certificate_photo'] = CertificatePhoto.objects.filter(paper_id=self.kwargs['Certificate_id'])
        # context['certificate_list'] = Certificate.objects.filter(person_id=self.kwargs['person_id'])
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

    bar = Bar("Bar chart", "precipitation and evaporation one year", height=2800)
    bar.add("2016", attr, v1, mark_line=["average"], mark_point=["max"])
    bar.add("2015", attr, v2, mark_line=["average"], mark_point=["max"])
    bar.add("2014", attr, v3, mark_line=["average"], mark_point=["max"],
            is_convert=True, yaxis_interval=0, )

    # print(bar._option)

    return bar