from django import template
from django.db.models import Count

from person.models import Certificate, CertificatesType


register = template.Library()


def display(areas):
    display_list = []

    for area in areas:
        q = {area.id : area.type_name}
        # display_list.append(area.id)
        # display_list.append(area.type_name)
        display_list.append(q)

        children = area.children.all()
        if len(children) > 0:
           display_list.append(display(children))

    return display_list


def get_dept_tree(areas):
    display_tree = []
    for p in areas:
        node = dict(id= p.id, text= p.type_name)
        # node.id = p.id
        # node.text = p.name
        children = p.children.all()
        if len(children) > 0:
            node.nodes = get_dept_tree(children)
        display_tree.append(node.to_dict())
    return display_tree


#
#
@register.inclusion_tag('certificate/certificates_type_tree_test.html')
def total_posts():
    areas = CertificatesType.objects.filter(parent_id=None)
    areas = get_dept_tree(areas)
    print(areas)
    return {'var': areas}





@register.inclusion_tag('certificate/certificates_type_tree_tags.html')
def category():
    category = CertificatesType.objects.annotate(
            num_article=Count('name'))
    # category = display(category)
    print(category)
    return {'categories': category}