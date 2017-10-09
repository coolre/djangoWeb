# coding: utf-8
import django_tables2 as tables
from .models import Contact, Contract,  WorkRecord, Certificate


class ContactTable(tables.Table):
    person = tables.RelatedLinkColumn()
    id = tables.Column(accessor='pk')

    class Meta:
        model = Contact
        attrs = {'class': 'table table-sm table-hover'}
        exclude = ('created_at', 'updated_at', 'address', 'state')
        # template = 'django_tables2/bootstrap.html'


class ContractTable(tables.Table):
    person = tables.RelatedLinkColumn()
    id = tables.Column(accessor='pk')

    class Meta:
        model = Contract
        attrs = {'class': 'table   table-sm table-hover'}
        exclude = ('created_at', 'updated_at','state')
        # template = 'django_tables2/bootstrap.html'




class WorkrecordTable(tables.Table):
    person = tables.RelatedLinkColumn()
    id = tables.Column(accessor='pk')
    # name = tables.LinkColumn()
    get_company = tables.Column()

    class Meta:
        model = WorkRecord
        attrs = {'class': 'table table-sm table-hover'}
        exclude = ('created_at', 'updated_at', 'state')
        # template = 'django_tables2/bootstrap.html'person


class CertificateTable(tables.Table):
    # person = tables.RelatedLinkColumn()
    certificates_name = tables.LinkColumn()

    class Meta:
        model = Certificate
        attrs = {'class': 'table table-bordered table-sm table-hover'}
        exclude = ('created_at', 'updated_at', 'state')
        # template = 'django_tables2/bootstrap.html'person