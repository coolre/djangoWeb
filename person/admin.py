#
from django.contrib import admin

from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportMixin, ExportActionModelAdmin

# Register your models here.
from .models import Person, Contact,Contract, Workrecord, CertificatesType, Certificate, CertificateRecod, CertificatePhoto, Salary


# Person
class PersonResource(resources.ModelResource):
    # mobile_title = fields.Field(column_name='mobile')

    class Meta:
        model = Person
        import_id_fields = ('id',)
        fields = ('id', 'name', 'identification', 'gender', 'rationality', 'hometown')

class PersonAdmin(ImportExportModelAdmin):
    """Customize the look of the auto-generated admin for the Member model"""
    fields = ('name', 'identification', 'gender', 'avatar')
    list_display = ('name', 'identification', 'gender', 'rationality', 'hometown','avatar')
    # list_editable = ['identification']
    # # inlines = [MobileInline, TelephoneInline, AddressInline, QqInline]
    list_filter = ('gender',)
    search_fields = ('name',)
    ordering = ('id',)
    resource_class = PersonResource


# Contact
class ContactResource(resources.ModelResource):
    person = fields.Field(
        column_name='person',
        attribute='person',
        widget=ForeignKeyWidget(Person, 'name'))

    class Meta:
        model = Contact
        # import_id_fields = ('id',)
        fields = ('id', 'person', 'mobile', 'telephone','telephone_short', 'email', 'qq', 'address',)
        export_order = ('id',)

class ContactAdmin(ImportExportModelAdmin):
    list_display = ('person', 'mobile', 'telephone','email', 'qq', 'address')
    search_fields = ('person__name',)
    resource_class = ContactResource


# Contract
class ContractResource(resources.ModelResource):
    person = fields.Field(
        column_name='person',
        attribute='person',
        widget=ForeignKeyWidget(Person, 'name'))

    class Meta:
        model = Contract
        # import_id_fields = ('id',)
        fields = ('id', 'person', 'company')
        export_order = ('id',)

class ContractAdmin(ImportExportModelAdmin):
    list_display = ( 'company', 'person', 'type', 'Contract_start_date', 'Contract_end_date')
    search_fields = ('person__name',)
    resource_class = ContractResource


# Workrecord
class WorkrecordAdmin(admin.ModelAdmin):
    list_display = ('person', 'company', 'project', 'department', 'Post', 'job_start_date', 'job_end_date')


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
        export_order = ('id', )
        # export_order = ('id', 'price', 'author', 'name')

class SalaryAdmin(ImportExportModelAdmin):
    list_display = ('person', 'pay_year', 'pay_month', 'pay_type', 'pay_money', 'belong_year', 'pay_use', 'state')
    list_filter = ( 'state', 'belong_year', 'pay_year', )
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
admin.site.register(Contract, ContractAdmin)
admin.site.register(Workrecord, WorkrecordAdmin)
admin.site.register(CertificatesType, CertificatesTypeAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(CertificateRecod)
admin.site.register(CertificatePhoto)
admin.site.register(Salary, SalaryAdmin)




