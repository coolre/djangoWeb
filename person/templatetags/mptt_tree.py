from django import template
from django.shortcuts import render, HttpResponse, render_to_response
from django.template.loader import render_to_string

register = template.Library()


# @register.simple_tag
@register.inclusion_tag('org_list.html', takes_context=True)
def tree_org(context):
    # areas = CertificatesType.objects.filter(parent_id=None)
    # .values_list("type_name", flat=True).distinct()
    # areas = display(areas)
    # {{var | unordered_list}}
    # areas = unordered_list
    # print(areas)

    # url = str("{% url 'persons:person_list' node.id %}")

    # url = template.Context({'url': "{% url 'persons:person_list' node.id %}"})

    # return render('org_list.html',  {'url': url})
    # return render_to_string('org_list.html',  {'url': url})
    # return mptt

    return {
        'link': 12,
        # 'title': context['home_title'],
    }