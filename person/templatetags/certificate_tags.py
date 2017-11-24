from django import template
from django.shortcuts import render_to_response

register = template.Library()

from ..models import Certificate, CertificatesType

def display(areas):
    display_list = []
    for area in areas:
        display_list.append(area.type_name)

        children = area.children.all()
        if len(children) > 0:
            display_list.append(display(children))
    return display_list



@register.simple_tag
def total_posts():
    areas = CertificatesType.objects.filter(parent_id=None)
    # .values_list("type_name", flat=True).distinct()
    # areas = display(areas)
    # {{var | unordered_list}}
    # areas = unordered_list
    print(areas)
    return render_to_response({'var': display(areas)})

