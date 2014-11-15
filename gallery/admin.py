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

def add_to_gallery(modeladmin, request, queryset):
    queryset.update(add_this_photo_to_gallery=True)
add_to_gallery.short_description = "Add marked photos to gallery"


def add_to_slider(modeladmin, request, queryset):
    queryset.update(add_this_photo_to_slide=True)
add_to_slider.short_description = "Add marked photos to slider"


class PhotoGalleryAdmin(MPTTModelAdmin, TranslationAdmin):
    list_display = ['image', 'title', 'description']
    search_fields = ['description_ru', 'description_en']
    list_filter = ['add_this_photo_to_slide', 'add_this_photo_to_gallery']
    form = MPTTAdminForm

    actions = [add_to_gallery, add_to_slider]

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
                'title',
                'description',
                'add_this_photo_to_slide',
                'add_this_photo_to_gallery',
            ]
        }),
    ]

class VideoGalleryAdmin(MPTTModelAdmin, TranslationAdmin):
    list_display = ['video', 'image', 'description', 'type']
    search_fields = ['description_ru', 'description_en' ]
    form = MPTTAdminForm

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
                'video_image',
                'description',
            ]
        }),
    ]

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        # c = Converter()

        filename = u''+obj.video.path

        ext = filename.split('.')[-1]
        # new_filename = filename[:-len(ext)]+'mp4'
        # c.convert(filename, new_filename,{
        #     'format': 'mp4',
        #     'audio': { 'codec': 'aac' },
        #     'video': { 'codec': 'h264' }
        # })
        obj.type = u'video/'+ext
        # obj.video.path = new_filename
        obj.save()
        return super(VideoGalleryAdmin, self).save_model(request, obj, form, change)

# from converter import Converter


admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(VideoGallery, VideoGalleryAdmin)