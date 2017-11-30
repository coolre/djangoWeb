# coding=UTF-8
from uuid import uuid4
from datetime import date, datetime


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



# 根据身份证计算出生年月日
def get_person_born(identification):
    born = datetime.strptime(str(identification[6:14]), "%Y%m%d")
    return born

# 身份证计算年龄
def get_person_age(identification):
    today = date.today()
    # born = get_person_born(identification)
    born = datetime.strptime(str(identification[6:14]), "%Y%m%d")
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age

