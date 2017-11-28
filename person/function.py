# coding=UTF-8
from uuid import uuid4
from datetime import date

from django.utils.translation import ugettext_lazy as _

# 上传文件命名
def file_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return format(filename)

# 计算年龄
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))