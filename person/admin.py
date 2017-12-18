#
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportMixin, ExportActionModelAdmin

# Register your models here.
from .models import (Person, Contact, Contract, WorkRecord, CertificatesType, Certificate,
                     CertificateRecod, CertificatePhoto, Salary, Education, TechnicalTitles)
from organization.models import (Department, Post,)



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
    raw_id_fields = ('certificate',)
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
        fields = ('id', 'person', 'company','start_date', 'end_date')
        export_order = ('id', 'company', 'person', 'type', 'start_date', 'end_date')

class ContractAdmin(ImportExportModelAdmin):
    list_display = ('company', 'person', 'type', 'start_date', 'end_date')
    list_filter = ('type','company', 'start_date')
    search_fields = ('person__name',)
    resource_class = ContractResource

#TechnicalTitles
class TechnicalTitlesResource(resources.ModelResource):
    person = fields.Field(
        column_name='person',
        attribute='person',
        widget=ForeignKeyWidget(Person, 'name'))
    titles = fields.Field(
        attribute='get_titles_display',
        column_name=_(u'titles'))

    class Meta:
        model = Contract
        fields = ('id', 'person', 'titles', 'specialty', 'rating_time', 'employed_time')
        export_order = ('id', 'person', 'titles', 'specialty', 'rating_time', 'employed_time')

class TechnicalTitlesAdmin(ImportExportModelAdmin):
    list_display = ('person', 'titles', 'specialty', 'rating_time', 'employed_time')
    list_filter = ('specialty',)
    search_fields = ('person__name',)
    raw_id_fields = ('certificate',)
    resource_class = TechnicalTitlesResource


# WorkRecord
class WorkRecordResource(resources.ModelResource):
    person = fields.Field(
        column_name='person',
        attribute='person',
        widget=ForeignKeyWidget(Person, 'name'))
    # company = fields.Field(
    #     column_name='company',
    #     attribute='company',
    #     widget=ForeignKeyWidget(Company, 'name'))
    # project = fields.Field(
    #     column_name='project',
    #     attribute='project',
    #     widget=ForeignKeyWidget(Project, 'name'))
    department = fields.Field(
        column_name='department',
        attribute='department',
        widget=ForeignKeyWidget(Department, 'name'))
    post = fields.Field(
        column_name='post',
        attribute='post',
        widget=ForeignKeyWidget(Post, 'name'))

    class Meta:
        model = WorkRecord
        fields = ('id',  'person', 'department', 'post', 'job_start_date', 'job_end_date')
        export_order = ('id', 'person','department', 'post', 'job_start_date', 'job_end_date')

class WorkRecordAdmin(ImportExportModelAdmin):
    # list_display = ('person', 'company', 'project', 'department', 'Post', 'job_start_date', 'job_end_date')
    list_display = ('person', 'department', 'post', 'job_start_date', 'job_end_date')
    list_filter = ('organization', 'department', 'post', 'job_start_date')
    search_fields = ('person__name',)
    resource_class = WorkRecordResource


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
        export_order = ('id', 'person', 'belong_year', 'pay_year', 'pay_month', 'pay_type', 'pay_money', 'pay_use' )


class SalaryAdmin(ImportExportModelAdmin):
    list_display = ('person', 'pay_year', 'pay_month', 'pay_type', 'pay_money', 'belong_year', 'pay_use', 'state')
    list_filter = ('state', 'belong_year', 'pay_year', )
    search_fields = ('person__name',)
    ordering = ('id',)
    resource_class = SalaryResource

from mptt.admin import DraggableMPTTAdmin
from django.utils.html import format_html
#
# class CertificatesTypeAdmin(admin.ModelAdmin):
#     # pass
#     list_display = ('type_name',)

class CertificatesTypeDraggableMPTTAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'something')
    list_display_links = ('something',)

    def something(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.type_name,  # Or whatever you want to put here
        )

    something.short_description = _('something nice')
admin.site.register(CertificatesType, CertificatesTypeDraggableMPTTAdmin)

# CertificateAdmin
class CertificatePhotoInline(admin.TabularInline):
    model = CertificatePhoto
    extra = 1

class CertificateRecodInline(admin.TabularInline):
    model = CertificateRecod
    extra = 1


class CertificateResource(resources.ModelResource):
    person = fields.Field(
        column_name='person',
        attribute='person',
        widget=ForeignKeyWidget(Person, 'name'))
    name = fields.Field(
        column_name='name',
        attribute='name',
        widget=ForeignKeyWidget(CertificatesType, 'type_name'))

    class Meta:
        model = Certificate
        # import_id_fields = ('person',)
        fields = ('id', 'person', 'name', 'number', 'issue_date', 'reg_date', 'expiry_date', 'issue')
        export_order = ('id', 'person', 'name', 'number', 'issue_date', 'reg_date', 'expiry_date', 'issue')


class CertificateAdmin(ImportExportModelAdmin):
    fields = ('person', ('name', 'number'), ('issue_date', 'reg_date', 'expiry_date'), 'issue')
    list_display = ('person', 'name', 'number', 'issue_date', 'reg_date', 'expiry_date', 'issue')
    list_filter = ('expiry_date',)
    inlines = [CertificatePhotoInline, CertificateRecodInline]
    raw_id_fields = ('person',)
    search_fields = ('person__name',)
    ordering = ('id',)
    resource_class = CertificateResource


#
class CertificateRecodAdmin(admin.ModelAdmin):
    fields = ('certificate', 'borrow_people', 'borrow_date', 'return_date', 'use')
    list_display = ('certificate', 'borrow_people', 'borrow_date', 'return_date', 'use')
    raw_id_fields = ('certificate',)

#
class CertificatePhotoAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'issue', 'photo')
    search_fields = ('certificate',)



admin.site.register(Person, PersonAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(TechnicalTitles, TechnicalTitlesAdmin)
admin.site.register(WorkRecord, WorkRecordAdmin)
# admin.site.register(CertificatesType, CertificatesTypeAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(CertificateRecod)
admin.site.register(CertificatePhoto, CertificatePhotoAdmin)
admin.site.register(Salary, SalaryAdmin)




