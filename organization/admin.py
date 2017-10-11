from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import  OrganizationTree, Department, Post


class CustomMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20
    mptt_indent_field = "name"


class MyDraggableMPTTAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'something')
    list_display_links = ('something',)

    def something(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,  # Or whatever you want to put here
        )

    something.short_description = _('something nice')



admin.site.register(OrganizationTree, MyDraggableMPTTAdmin)





class PostAdmin(admin.ModelAdmin):
    pass

    class Meta:
        model = Post


class DepartmentAdmin(admin.ModelAdmin):
    pass

    class Meta:
        model = Department


admin.site.register(Post, PostAdmin)
admin.site.register(Department, DepartmentAdmin)