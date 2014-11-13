# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel

from fields import ExtFileField


class PhotoGallery(MPTTModel):
    parent = models.ForeignKey('self', null=True, blank=True, related_name="related")
    photo = ExtFileField(upload_to='photos', verbose_name=_("Image"),
                             ext_whitelist=(".png", ".jpg", ".PNG", ".JPG", ".jpeg", ".JPEG"))
    description = models.CharField(max_length=255, blank=True, verbose_name=_("Description"))
    title = models.CharField(max_length=255, blank=True, verbose_name=_("Title"))
    add_this_photo_to_slide = models.BooleanField(null=False, verbose_name=_(u"Add this photo to slide"))
    add_this_photo_to_gallery = models.BooleanField(null=False, verbose_name=_(u"Add this photo to gallery"))

    def __unicode__(self):
        return self.photo.name

    class Meta:
        verbose_name = _(u"Photo")
        verbose_name_plural = _(u"Photos")


import random


def get_path_and_name(instance, filename):
    print instance, filename
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    instance.filename =  u'videos/'+u''.join(random.choice(letters) for x in xrange(31))+u'_c.'+filename.split('.')[-1]
    return instance.filename

class VideoGallery(MPTTModel):
    parent = models.ForeignKey('self', null=True, blank=True, related_name="related")
    video = ExtFileField(upload_to=get_path_and_name, verbose_name=_("video"),
                         ext_whitelist=(".mp4", ".ogg", ".webm", ".MP4", ".OGG", ".WEBM",),)
    video_image = ExtFileField(upload_to='videos/images', verbose_name=_("Image"),
                             ext_whitelist=(".png", ".jpg", ".PNG", ".JPG", ".jpeg", ".JPEG"),
                             default="css/images/slide3.png")

    description = models.CharField(max_length=255, blank=True, verbose_name=_("Description"))
    add_this_photo_to_gallery = models.BooleanField(null=False, verbose_name=_(u"Add this photo to gallery"))
    type = models.CharField(verbose_name=_("Extension of video"), max_length=15, default='video/mp4')

    def __unicode__(self):
        return ("%s - %s")%(self.video, self.type)


    class Meta:
        verbose_name = _(u"Video")
        verbose_name_plural = _(u"Videos")


