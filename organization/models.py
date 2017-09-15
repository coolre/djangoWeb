from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangoWeb.models import AbstractBaseModel

# Create your models here.
from treebeard.mp_tree import MP_Node
from mptt.models import MPTTModel, TreeForeignKey


# 架构
class OrganizationTree(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']


class Company(MP_Node):
    name = models.CharField(max_length=100)
    node_order_by = ['name']

    class Meta:
        verbose_name = _('公司名称')
        verbose_name_plural = _('公司名称')

    def __str__(self):
        return '%s' % self.name


class Project(AbstractBaseModel):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company)

    class Meta:
        verbose_name = _('项目名称')
        verbose_name_plural = _('项目名称')

    def __str__(self):
        return '%s' % self.name


# Department
class Department(AbstractBaseModel):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company)
    # belong = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('部门名称')
        verbose_name_plural = _('部门名称')

    def __str__(self):
        return self.name


class Post(AbstractBaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('岗位名称')
        verbose_name_plural = _('岗位名称')

    def __str__(self):
        return self.name


class Job(AbstractBaseModel):
    name = models.CharField(max_length=100)
    tes = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('职务名称')
        verbose_name_plural = _('职务名称')

    def __str__(self):
        return self.name

