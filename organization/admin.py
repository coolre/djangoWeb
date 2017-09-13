from django.contrib import admin

# Register your models here.
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Company, Project, Department, Post


class CompanyAdmin(TreeAdmin):
     form = movenodeform_factory(Company)


# admin
class ProjectAdmin(admin.ModelAdmin):
    pass

    class Meta:
        model = Project


class DepartmentAdmin(admin.ModelAdmin):
    pass

    class Meta:
        model = Department


class PostAdmin(admin.ModelAdmin):
    pass

    class Meta:
        model = Post


admin.site.register(Company, CompanyAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Post, PostAdmin)