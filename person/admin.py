#
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportMixin, ExportActionModelAdmin

# Register your models here.
from .models import (Person, Contact, Contract, Workrecord, CertificatesType, Certificate,
                     CertificateRecod, CertificatePhoto, Salary, Education)
from organization.models import (Company, Project, Department, Post)


# Person
class PersonResource(resources.ModelResource):
    gender = fields.Field(
        attribute='get_gender_display',
        column_name=_(u'gender'))

    class Meta:
        model = Person
        # import_id_fields = ('id',)
        fields = ('id', 'name', 'identification', 'gender', 'rationality', 'hometown')
        export_order = ('id', 'name', 'identification', 'gender', 'rationality', 'hometown')

class PersonAdmin(ImportExportModelAdmin):
    list_display = ('name', 'identification', 'gender', 'rationality', 'hometown', 'avatar')
    # list_editable = ['identification']
    # # inlines = [MobileInline, TelephoneInline, AddressInline, QqInline]
    list_filter = ('gender',)
    search_fields = ('name',)
    ordering = ('id',)
    resource_class = PersonResource


# Education
class EducationResource(resources.ModelResource):
    person = fields.Field(
        column_name='person',
        attribute='person',
        widget=ForeignKeyWidget(Person, 'name'))
    level = fields.Field(
        attribute='get_level_display',
        column_name=_(u'level'))
    type = fields.Field(
        attribute='get_type_display',
        column_name=_(u'type'))

    class Meta:
        model = Education
        fields = ('id', 'person', 'level', 'School', 'major', 'type', 'length', 'graduation_date',)
        export_order = ('id',)

class EducationAdmin(ImportExportModelAdmin):
    list_display = ('person', 'level', 'School', 'major', 'type', 'length', 'graduation_date',)
    search_fields = ('person__name',)
    resource_class = EducationResource


# Contact
class ContactResource(resources.ModelResource):
    person = fields.Field(
        column_name='person',
        attribute='person',
        widget=ForeignKeyWidget(Person, 'name'))

    class Meta:
        model = Contact
        # import_id_fields = ('id',)
        fields = ('id', 'person', 'mobile', 'telephone', 'telephone_short', 'email', 'qq', 'address',)
        export_order = ('id', 'person', 'mobile', 'telephone', 'telephone_short', 'email', 'qq', 'address',)

class ContactAdmin(ImportExportModelAdmin):
    list_display = ('person', 'mobile', 'telephone', 'telephone_short', 'email', 'qq', 'address')
    search_fields = ('person__name',)
    resource_class = ContactResource


# Contract
class ContractResource(resources.ModelResource):
    person = fields.Field(
        column_name='person',
        attribute='person',
        widget=ForeignKeyWidget(Person, 'name'))
    type = fields.Field(
        attribute='get_type_display',
        column_name=_(u'type'))

    class Meta:
        model = Contract
        fields = ('id', 'person', 'company')
        export_order = ('id', 'company', 'person', 'type', 'Contract_start_date', 'Contract_end_date')

class ContractAdmin(ImportExportModelAdmin):
    list_display = ('company', 'person', 'type', 'Contract_start_date', 'Contract_end_date')
    search_fields = ('person__name',)
    resource_class = ContractResource


# Workrecord
class WorkrecordResource(resources.ModelResource):
    person = fields.Field(
        column_name='person',
        attribute='person',
        widget=ForeignKeyWidget(Person, 'name'))
    company = fields.Field(
        column_name='company',
        attribute='company',
        widget=ForeignKeyWidget(Company, 'name'))
    project = fields.Field(
        column_name='project',
        attribute='project',
        widget=ForeignKeyWidget(Project, 'name'))
    department = fields.Field(
        column_name='department',
        attribute='department',
        widget=ForeignKeyWidget(Department, 'name'))
    post = fields.Field(
        column_name='Post',
        attribute='Post',
        widget=ForeignKeyWidget(Post, 'name'))

    class Meta:
        model = Workrecord
        fields = ('id',  'person', 'company', 'project', 'department', 'post', 'job_start_date', 'job_end_date')
        export_order = ('id', 'person', 'company', 'project', 'department', 'post', 'job_start_date', 'job_end_date')

class WorkrecordAdmin(ImportExportModelAdmin):
    # list_display = ('person', 'company', 'project', 'department', 'Post', 'job_start_date', 'job_end_date')
    list_display = ('person', 'company', 'project', 'department', 'post', 'job_start_date', 'job_end_date')
    search_fields = ('person__name',)
    resource_class = WorkrecordResource


# Salary
class SalaryResource(resources.ModelResource):
    person = fields.Field(
        column_name='person',
        attribute='person',
        widget=ForeignKeyWidget(Person, 'name'))

    class Meta:
        model = Salary
        # import_id_fields = ('person',)
        fields = ('id', 'person', 'belong_year', 'pay_year', 'pay_month', 'pay_type', 'pay_money', 'pay_use')
        export_order = ('id','person', 'belong_year', 'pay_year', 'pay_month', 'pay_type', 'pay_money', 'pay_use' )


class SalaryAdmin(ImportExportModelAdmin):
    list_display = ('person', 'pay_year', 'pay_month', 'pay_type', 'pay_money', 'belong_year', 'pay_use', 'state')
    list_filter = ('state', 'belong_year', 'pay_year', )
    search_fields = ('person__name',)
    ordering = ('id',)
    resource_class = SalaryResource


class CertificatesTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'issue')


class CertificatePhotoInline(admin.TabularInline):
    model = CertificatePhoto
    extra = 1

class CertificateRecodInline(admin.TabularInline):
    model = CertificateRecod
    extra = 1

class CertificateAdmin(admin.ModelAdmin):
    fields = ('person', ('certificates_type', 'issue_date', 'reg_date', 'expiry_date'))
    inlines = [CertificatePhotoInline, CertificateRecodInline]
    raw_id_fields = ('person',)


#
class CertificateRecodAdmin(admin.ModelAdmin):
    list_display = ('person', 'borrow_people', 'borrow_date', 'return_date', 'use_project', 'use')

#
class CertificatePhotoAdmin(admin.ModelAdmin):
    list_display = ('person', 'name', 'photo')



admin.site.register(Person, PersonAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Workrecord, WorkrecordAdmin)
admin.site.register(CertificatesType, CertificatesTypeAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(CertificateRecod)
admin.site.register(CertificatePhoto)
admin.site.register(Salary, SalaryAdmin)




