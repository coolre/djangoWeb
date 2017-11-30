# coding=UTF-8
from django import template

from pyecharts import Bar, Page, Style
from pyecharts import Bar

from person.models import Person
from person.function import get_person_age

register = template.Library()


@register.inclusion_tag('home/tags_charts_ages.html', takes_context=True)
def chartsAges(context):
    #年龄段人数
    def get_v(gender):
        c20 = 0
        c21 = 0
        c26 = 0
        c31 = 0
        c36 = 0
        c41 = 0
        c46 = 0
        c51 = 0
        c56 = 0
        c60 = 0
        person_data = Person.objects.all().filter(gender=gender)
        for data in person_data:
            card = data.identification
            age = get_person_age(card)
            if age <= 20:
                c20 += 1
            if 20 < age <= 25:
                c21 += 1
            if 25 < age <= 30:
                c26 += 1
            if 30 < age <= 35:
                c31 += 1
            if 35 < age <= 40:
                c36 += 1
            if 40 < age <= 45:
                c41 += 1
            if 45 < age <= 50:
                c46 += 1
            if 50 < age <= 55:
                c51 += 1
            if 55 < age <= 60:
                c56 += 1
            if 60 < age:
                c60 += 1
        return [c20, c21, c26, c31, c36, c41, c46, c51, c56, c60]

    def create_charts():
        page = Page()
        style = Style(
            width=600, height=350
            )
        attr = ["20以下", "21-25", "26-30", "31-35", "36-40", "40-45", "46-50", "51-55", "56-60", "60以上"]
        v1 = get_v('Male')
        v2 = get_v('Female')
        chart = Bar("性别-年龄结构", **style.init_style)
        chart.add("男", attr, v1, is_stack=True, is_label_show=True, label_pos="inside", label_text_color="#fff",)
        chart.add("女", attr, v2, is_stack=True, is_label_show=True, label_color =["#2f4554","#c13530"], )
        page.add(chart)
        return page

    charts =create_charts().render_embed()
    return {'echart': charts}

