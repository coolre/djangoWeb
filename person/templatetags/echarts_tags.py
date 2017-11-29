# coding=UTF-8
from django import template

from pyecharts import Bar, Page, Style
from pyecharts import Bar

from person.models import Person


register = template.Library()


@register.inclusion_tag('home/tags_charts_ages.html', takes_context=True)
def chartsAges(context):

    def get_male_age():
        data = Person.objects.filter(gender='male')

        for list in data:
            list.age = Person.get_age(list.id)
        print('data')
        return data

    def get_female_age():
        data = Person.objects.filter(gender='female')
        return dict(data)


    def create_charts():
        page = Page()

        style = Style(
            width=600, height=350
        )

        attr = ["20以下", "21-25", "26-30", "31-35", "36-40", "40-45", "46-50", "51-55", "56-60", "60以上"]
        v1 = [5, 20, 36, 10, 75, 90, 36, 10, 75, 90]
        v2 = [10, 25, 8, 60, 20, 80, 36, 10, 75, 90]

        chart = Bar("性别-年龄结构", **style.init_style)
        chart.add("女", attr, v1, is_stack=True)
        chart.add("男", attr, v2, is_stack=True)
        page.add(chart)
        return page

    chartsAges =create_charts().render_embed()
    return {'echart': chartsAges}

#
# @register.inclusion_tag('home/tags_charts_ages.html', takes_context=True)
# def chartsAges(context):
#     def create_charts():
#         page = Page()
#
#         style = Style(
#             width=600, height=350
#         )
#
#         attr = ["20以下", "21-25", "26-30", "31-35", "36-40", "40-45", "46-50", "51-55", "56-60", "60以上"]
#         v1 = [5, 20, 36, 10, 75, 90, 36, 10, 75, 90]
#         v2 = [10, 25, 8, 60, 20, 80, 36, 10, 75, 90]
#         chart = Bar("性别-年龄结构", **style.init_style)
#         chart.add("女", attr, v1, is_stack=True)
#         chart.add("男", attr, v2, is_stack=True)
#         page.add(chart)
#         return page
#
#     chartsAges =create_charts().render_embed()
#     return {'echart': chartsAges}
