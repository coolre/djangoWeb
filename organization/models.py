from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from djangoWeb.models import AbstractBaseModel

# Create your models here.
from mptt.models import MPTTModel, TreeForeignKey


# 架构   工作机构
class OrganizationTree(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('组织架构')
        verbose_name_plural = _('组织架构')

    def get_absolute_url(self):
        # return "/"
        # return reverse('show_genres', kwargs={'pk': self.pk, })
        return reverse('organization:person_list', kwargs={'pk': self.pk, })

    def __str__(self):
        return "%s" % self.name


#
# Department
class Department(AbstractBaseModel):
    name = models.CharField(max_length=100)
    order_num = models.IntegerField(default=0)
    belong = TreeForeignKey(OrganizationTree, related_name="dep", verbose_name=_("所属机构"), blank=True, null=True)

    class Meta:
        verbose_name = _('部门名称')
        verbose_name_plural = _('部门名称')

    def __str__(self):
        return self.name


class Post(AbstractBaseModel):
    name = models.CharField(max_length=100)
    order_num = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('岗位名称')
        verbose_name_plural = _('岗位名称')

    def __str__(self):
        return self.name



