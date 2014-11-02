# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel

from fields import ExtFileField

class PhotoGallery(MPTTModel):
    parent = models.ForeignKey('self', null=True, blank=True, related_name="related")
    photo = ExtFileField(upload_to='photos', verbose_name=_("Image"),
                             ext_whitelist=(".png", ".jpg", ".PNG", ".JPG", ".jpeg", ".JPEG"))
    description= models.CharField(max_length=255, blank=True, verbose_name=_("Description"))
    add_this_photo_to_slide = models.BooleanField(null=False, verbose_name=_(u"Add this photo to slide"))
    add_this_photo_to_gallery = models.BooleanField(null=False, verbose_name=_(u"Add this photo to gallery"))

    def __unicode__(self):
        return self.photo.name

    class Meta:
        verbose_name = _(u"Photo")
        verbose_name_plural = _(u"Photos")


class VideoGallery(MPTTModel):
    parent = models.ForeignKey('self', null=True, blank=True, related_name="related")
    video = ExtFileField(upload_to='videos', verbose_name=_("video"),
                         ext_whitelist=(".mp4", ".ogg", ".webm", ".MP4", ".OGG", ".WEBM",))
    video_image = ExtFileField(upload_to='videos/images', verbose_name=_("Image"),
                             ext_whitelist=(".png", ".jpg", ".PNG", ".JPG", ".jpeg", ".JPEG"))
    description = models.CharField(max_length=255, blank=True, verbose_name=_("Description"))
    add_this_photo_to_gallery = models.BooleanField(null=False, verbose_name=_(u"Add this photo to gallery"))

    def __unicode__(self):
        return ("%s - %s")%(self.video, self.description)

    class Meta:
        verbose_name = _(u"Video")
        verbose_name_plural = _(u"Videos")


