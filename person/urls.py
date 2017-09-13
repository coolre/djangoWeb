from django.conf.urls import url, include

from .views import charts
#
# urlpatterns = [
#     url(r'^$', HomePageView.as_view(), name='home'),
# ]

# from django.conf.urls import patterns, include, url
from .views import index, PersonListView, PersonDetailView, contact, contract, workrecord, certificate, CertificateDetailView, SalaryChartsView, SalaryBarView


urlpatterns = [

    url(r'^$', index, name='index'),
    # url(r'^$', PersonListView.as_view(), name='list'),
    url(r'^(?P<person_id>\d+)/$', PersonDetailView.as_view(), name='detail'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^contract/$', contract, name='contract'),
    url(r'^workrecord/$', workrecord, name='workrecord'),
    url(r'^certificate/$', certificate, name='certificate'),
    url(r'^certificate/(?P<Certificate_id>\d+)/$', CertificateDetailView.as_view(), name='certificate_detail'),

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