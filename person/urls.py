from django.conf.urls import url, include

from .views import charts
from . import views
#
# urlpatterns = [
#     url(r'^$', HomePageView.as_view(), name='home'),
# ]

# from django.conf.urls import patterns, include, url
# from .views import （index, PersonDetailView, contact, contract, workrecord, certificate, CertificateDetailView, SalaryChartsView, SalaryBarView, ShowOrgPersonsListView, ShowOrgPersonscontactListView, ShowTypeCertificateListView）


app_name = 'persons'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^$', PersonListView.as_view(), name='list'),
    url(r'^(?P<person_id>\d+)/$', views.PersonDetailView.as_view(), name='detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contract/$', views.contract, name='contract'),
    url(r'^workrecord/$', views.workrecord, name='workrecord'),
    url(r'^certificate/$', views.certificate, name='certificate'),
    url(r'^certificate/(?P<Certificate_id>\d+)/$', views.CertificateDetailView.as_view(), name='certificate_detail'),

    url(r'workbyorg/(?P<pk>\d+)', views.ShowOrgPersonsListView.as_view(), name="person_list",),
    url(r'contactbyorg/(?P<pk>\d+)', views.ShowOrgPersonscontactListView.as_view(), name="person_contact_list", ),

    # url(r'certificatebytype/(?P<pk>\d+)', views.ShowTypeCertificateListView.as_view(), name="certificate_type_list",),


    url(r'^typecertificate/(?P<CertificatesType_id>\d+)', views.TypeCertificateList.as_view(), name="certificate_type_list"),

    # # Column
    # url(r'^column_chart/$', views.column_chart, name='column_chart'),
    # url(r'column_chart/simpleBar/', views.SimpleBarView.as_view()),
    # url(r'^column_highchart/json/$', views.column_highchart_json,
    #     name='column_highchart_json'),
    # # Line chart
    # url(r'^line_chart/$', views.line_chart,
    #     name='line_chart'),
    # url(r'^line_chart/json/$', views.line_chart_json,
    #     name='line_chart_json'),
    # url(r'^line_highchart/json/$', views.line_highchart_json,
    #     name='line_highchart_json'),

    # url(r'^salarycharts/$', SalaryChartsView.as_view()),
    # url(r'json/SalaryBar/', SalaryBarView.as_view(), name='SalaryBarView')
    url(r'^charts/$', charts, name='charts'),
    ]