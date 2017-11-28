from django import template
from django.db.models import Count

from organization.models import OrganizationTree
from person.models import CertificatesType

register = template.Library()


@register.inclusion_tag('org_list.html', takes_context=True)
def tree_org(context):
    nodes = OrganizationTree.objects.all()
    return {'nodes': nodes}


@register.inclusion_tag('certificate/certificates_type_tree.html', takes_context=True)
def tree_certificates_type(context):
    nodes = CertificatesType.objects.all()
    genre = nodes[0]
    print(nodes)
    return {'nodes': nodes, 'genre': genre}

