# coding=UTF-8
from uuid import uuid4
from datetime import date, datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from djangoWeb.models import AbstractBaseModel
from organization.models import (Company, Project, Department, Post)

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


# models Person.人员
class Person(AbstractBaseModel):
    GENDER_CHOICES = (
        ('Male', '男'),
        ('Female', '女'),
    )

    def avatar_file_name(instance, filename):
        new_name = file_rename(instance, filename)
        person_id = instance.id
        return 'person/%s/avatars_%s' % (person_id, new_name)

    name = models.CharField(_("姓名"), max_length=250)
    identification = models.CharField(_("身份证号"), max_length=18, unique=True)
    gender = models.CharField(_("性别"), max_length=10, choices=GENDER_CHOICES, default='male')
    rationality = models.CharField(_("民族"), max_length=250)
    hometown = models.CharField(_("籍贯"), max_length=250)
    avatar = models.ImageField(_("证件照"), upload_to=avatar_file_name, blank=True)
    # avatar = models.ImageField(upload_to=path_and_rename('person/avatars/'),)

    class Meta:
        verbose_name = _('人员')
        verbose_name_plural = _('人员')

    def __str__(self):
        return '%s' % self.name
        # return '%s <%s>' % (self.name, self.identification)

    def get_birthday(self):
        return int(self.identification[6:14])

    def get_age(self):
        born = datetime.strptime(str(self.identification[6:14]), "%Y%m%d")
        age = calculate_age(born)
        return age

    def get_person_name(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
        # return '%d/' % self.pk

# Education学历
class Education(AbstractBaseModel):
    LEVEL_CHOICES = (
        ('0', '无'),
        ('1', '高中'),
        ('2', '中(职)专'),
        ('3', '大专'),
        ('4', '本科'),
        ('5', '硕士研究生'),
        ('6', '博士'),
    )
    TYPE_CHOICES = (
        ('0', '全日制'),
        ('1', '继续教育'),
        ('2', '其他'),
    )
    person = models.ForeignKey(Person, verbose_name=_("姓名"), on_delete=models.CASCADE, )
    level = models.CharField(_('学历'), max_length=10, choices=LEVEL_CHOICES, default='0')
    School = models.CharField(_('学校'), max_length=255, blank=True, null=True)
    major = models.CharField(_('专业'), max_length=255, blank=True, null=True)
    type = models.CharField(_('类型'), max_length=10, choices=TYPE_CHOICES, blank=True,)
    length = models.CharField(_('年限'), max_length=255, blank=True, null=True)
    graduation_date = models.DateField(_("毕业时间"), blank=True, null=True)


    class Meta:
        verbose_name = _('学历情况')
        verbose_name_plural = _('学历情况')



# contact联系方式
class Contact(AbstractBaseModel):
    person = models.ForeignKey(Person, verbose_name=_("姓名"), on_delete=models.CASCADE,)
    address = models.CharField(_("地址"), max_length=100, blank=True)
    mobile = models.CharField(_("手机"), max_length=12, blank=True)
    telephone = models.CharField(_("固定电话"), max_length=12, blank=True)
    telephone_short = models.CharField(_("小号"), max_length=5, blank=True)
    email = models.EmailField(_("邮箱"), max_length=75, blank=True)
    qq = models.CharField(_("QQ"), max_length=13, blank=True)

    class Meta:
        verbose_name = _('联系方式')
        verbose_name_plural = _('联系方式')

    # def get_absolute_url(self):
    #     return '%d/' % self.pk

# contract劳动合同
class Contract(AbstractBaseModel):
    TYPE_CHOICES = (
        ('0', '有固定期限'),
        ('1', '无固定期限'),
    )
    person = models.ForeignKey(Person, verbose_name=_("乙方"))
    company = models.ForeignKey(Company, verbose_name=_("甲方"))
    type = models.CharField(_('合同类型'), max_length=10, choices=TYPE_CHOICES, default='0')
    Contract_start_date = models.DateField(_("开始时间"))
    Contract_end_date = models.DateField(_("结束时间"), blank=True, null=True)

    class Meta:
        verbose_name = _('劳动合同')
        verbose_name_plural = _('劳动合同')

    def __str__(self):
        return '%s' % self.person


# Workrecord工作记录
class Workrecord(AbstractBaseModel):
    person = models.ForeignKey(Person, verbose_name=_("姓名"))
    company = models.ForeignKey(Company, verbose_name=_("公司"))
    project = models.ForeignKey(Project, verbose_name=_("项目部"))
    department = models.ForeignKey(Department, verbose_name=_("部门"))
    post = models.ForeignKey(Post, verbose_name=_("岗位"))
    job_start_date = models.DateField(_("开始时间"))
    job_end_date = models.DateField(_("结束时间"), blank=True, null=True)
    # position = models.CharField(max_length=64)

    class Meta:
        verbose_name = _('工作经历')
        verbose_name_plural = _('工作经历')

    def __str__(self):
        return '%s' % self.person

    # def get_absolute_url(self):
    #     return reverse('PersonDetailView', args=[str(self.id)])

    # def get_company_person(company_id):
    #     data_person = Workrecord.objects.filter(company__id="company_id")
    #     # print(data_person)
    #     return data_person


class CertificatesType(models.Model):
    name = models.CharField(_('证件类别'), max_length=100, blank=True, null=True)
    type = models.CharField(_('类型'), max_length=100, blank=True, null=True)
    issue = models.CharField(_('备注'), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _('证件类别')
        verbose_name_plural = _('证件类别')

    def __str__(self):
        return '%s' % self.name


class Certificate(AbstractBaseModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_("姓名"))
    certificates_type = models.ForeignKey(CertificatesType, on_delete=models.CASCADE, verbose_name=_("证件名称"))
    issue_date = models.DateField(_("发证时间"))
    reg_date = models.DateField(_("登记时间"), blank=True, null=True)
    expiry_date = models.DateField(_("有效期"), blank=True, null=True)

    class Meta:
        verbose_name = _('证件')
        verbose_name_plural = _('证件')

    def __str__(self):
        return '%s-%s' % (self.person, self.certificates_type)

    def get_absolute_url(self):
        return reverse("certificate_detail", args=[self.id])


class CertificateRecod(AbstractBaseModel):
    paper = models.ForeignKey(Certificate, related_name='CertificateRecod', verbose_name=_("证件名称"))
    borrow_people = models.CharField(_("借用人"), max_length=80)
    borrow_date = models.DateField(_("借用时间"), )
    return_date = models.DateField(_("归还时间"), blank=True, null=True)
    use_project = models.ForeignKey(Project, verbose_name=_("使用单位"))
    use = models.CharField(_("备注"), max_length=160, blank=True,)

    class Meta:
        verbose_name = _('证件使用记录')
        verbose_name_plural = _('证件使用记录')

    def __str__(self):
        return '%s' % self.use_project


# def Certificate_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.paper.id, filename)
# def certificate_file_name(instance, filename):
#     return 'person/certificate_{0}/{1}'.format(instance.paper.id, filename)
    # return 'person/'.join(['certificatePhoto', instance.paper.id, filename])

class CertificatePhoto(AbstractBaseModel):

    def certificate_file_name(instance, filename):
        new_name = file_rename(instance, filename)
        person_id = instance.paper.person.id
        certificates_type_id = instance.paper.certificates_type.id
        return 'person/%s/certificate/%s_%s' % (person_id, certificates_type_id, new_name)

    paper = models.ForeignKey(Certificate, related_name='CertificatePhoto', verbose_name=_("证件名称"))
    name = models.CharField(_("图片说明"), max_length=100, blank=True, null=True)
    photo = models.ImageField(_("图片"), upload_to=certificate_file_name,)

    class Meta:
        verbose_name = _('证件图片')
        verbose_name_plural = _('证件图片')

    def __str__(self):
        return '%s' % self.name


class Salary(AbstractBaseModel):
    TYPE_CHOICES = (
        ('1', '月度工资'),
        ('2', '奖励'),
        ('3', '预兑现'),
        ('4', '兑现余额'),
        ('5', '资质补贴'),
        ('6', '其他'),
    )
    YEAR_CHOICES = (
        ('2014', '2014年'),
        ('2015', '2015年'),
        ('2016', '2016年'),
        ('2017', '2017年'),
        ('2018', '2018年'),
    )
    MONTH_CHOICES = (
        ('1', '1月'),
        ('2', '2月'),
        ('3', '3月'),
        ('4', '4月'),
        ('5', '5月'),
        ('6', '6月'),
        ('7', '7月'),
        ('8', '8月'),
        ('9', '9月'),
        ('10', '10月'),
        ('11', '11月'),
        ('12', '12月'),
    )
    person = models.ForeignKey(Person, verbose_name=_("姓名"))
    belong_year = models.CharField(_("归集年度"), max_length=10, choices=YEAR_CHOICES)
    pay_year = models.CharField(_("发放年度"), max_length=10, choices=YEAR_CHOICES)
    pay_month = models.CharField(_("发放月份"), max_length=10,  choices=MONTH_CHOICES)
    pay_type = models.CharField(_("类别"), max_length=10, choices=TYPE_CHOICES, default='1')
    pay_money = models.FloatField(_("金额"))
    pay_use = models.TextField(_("备注"), blank=True,)

    class Meta:
        verbose_name = _('薪资发放')
        verbose_name_plural = _('薪资发放')

    def __str__(self):
        return '%s' % self.pay_money


