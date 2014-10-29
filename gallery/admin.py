# coding: utf-8
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from modeltranslation.admin import TranslationAdmin
from mptt.forms import forms
import os

from models import PhotoGallery, VideoGallery
from seafoodservice import settings

class MPTTAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MPTTAdminForm, self).__init__(*args, **kwargs)


class PhotoGalleryAdmin(MPTTModelAdmin, TranslationAdmin):
    list_display = ['image', 'description']
    search_fields = ['description_ru', 'description_en']
    list_filter = ['add_this_photo_to_slide', 'add_this_photo_to_gallery']
    form = MPTTAdminForm

    def image(self, obj):
        return '<span style="width:20px;height:20px;"><img style="width:80px;height:80px;" src="%s" /></span>' % (settings.MEDIA_URL+obj.photo.name)
    image.allow_tags = True

    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

    fieldsets = [
        (None, {
            'fields': [
                'photo',
                'description',
                'add_this_photo_to_slide',
                'add_this_photo_to_gallery',
            ]
        }),
    ]

class VideoGalleryAdmin(MPTTModelAdmin, TranslationAdmin):
    list_display = ['video', 'description']
    search_fields = ['description_ru', 'description_en' ]

    def image(self, obj):
        return '<span style="width:200px;height:120px;"><img src="%s" /></span>'%(settings.MEDIA_URL+obj.photo.name)
    image.allow_tags = True

    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

    fieldsets = [
        (None, {
            'fields': [
                'video',
                'description',
            ]
        }),
    ]

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        filename = obj.video.path
        ext = os.path.splitext(filename)[1]
        obj.type = ext.lower()
        obj.save()

admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(VideoGallery, VideoGalleryAdmin)