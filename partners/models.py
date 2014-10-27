# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models

class Partner(models.Model):
    company_name = models.CharField(max_length=255, verbose_name=_("Company name"))
    logotype = models.ImageField(upload_to='images/service', verbose_name=_("Logo"))

    def __unicode__(self):
        return u'%s' % (self.company_name)

    class Meta:
        verbose_name = _(u"Partner")
        verbose_name_plural = _(u"Partners")