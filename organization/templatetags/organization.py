from django import template

# from ..models import Entry
from person.models import WorkRecord, Certificate

register = template.Library()

@register.inclusion_tag('org_list_person.html')
def render_month_links(p):
    return {
        'certificate' : Certificate.objects.filter(organization=p).values_list('name', flat=True)
    }



# @register.inclusion_tag('blog/entry_snippet.html')
# def render_latest_blog_entries(num, summary_first=False, hide_readmore=False, header_tag=''):
#     entries = Entry.objects.published()[:num]
#     return {
#         'entries': entries,
#         'summary_first': summary_first,
#         'header_tag': header_tag,
#         'hide_readmore': hide_readmore,
#     }

#
# @register.inclusion_tag('blog/month_links_snippet.html')
# def render_month_links():
#     return {
#         'dates': Entry.objects.published().dates('pub_date', 'month', order='DESC'),
#     }