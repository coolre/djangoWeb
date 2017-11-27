from django import template
from django.shortcuts import render, HttpResponse, render_to_response
from django.template.loader import render_to_string

from organization.models import OrganizationTree

register = template.Library()

#
# # @register.simple_tag
@register.inclusion_tag('org_list.html', takes_context=True)
def tree_org(context):
    nodes = OrganizationTree.objects.all()
    return {'nodes': nodes}
