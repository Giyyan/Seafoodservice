# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models

class GeograohyTransporation(models.Model):
    title = models.CharField(verbose_name=_(u"Title"), max_length=255)
    description = models.CharField(verbose_name=_(u"Description"), max_length=255)
    # point = models.PointField(verbose_name=_(u"Point"))