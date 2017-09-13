from django.db import models
from django.utils.translation import ugettext_lazy as _

STATE_CHOICES = (
        ('0', '有效'),
        ('1', '失效'),
    )

class AbstractBaseModel(models.Model):
    """AbstractBaseModel contains common fields between models.
    All models should extend this class.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.CharField(_("State"), choices=STATE_CHOICES, default=0, max_length=10)

    class Meta:
        abstract = True