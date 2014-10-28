# coding: utf-8
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from models import News, UsefullInformation, MainPage
from seafoodservice import settings


class NewsAdmin(SummernoteModelAdmin):
    search_fields = ['title_ru', 'title_en', 'body_ru', 'body_en' ]
    list_display = ('image', 'title', 'body_as_html')

    def body_as_html(self, obj):
        return obj.body
    body_as_html.allow_tags = True

    def image(self, obj):
        return '<span style="width:20px;height:20px;"><img style="width:80px;height:80px;" src="%s" /></span>' % (settings.MEDIA_URL+obj.title_image.name)
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
                'title_image',
                'title_ru',
                'body_ru',
                'title_en',
                'body_en',
            ]
        }),
    ]


class InformationAdmin(SummernoteModelAdmin):
    search_fields = ['title_ru', 'title_en', 'body_ru', 'body_en' ]
    list_display = ('title', 'body_as_html')

    def body_as_html(self, obj):
        return obj.body
    body_as_html.allow_tags = True

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
                'title_ru',
                'body_ru',
                'title_en',
                'body_en',
                ]
        }),
    ]


class MainPageAdmin(SummernoteModelAdmin):
    search_fields = ['body_ru', 'body_en' ]
    list_display = ['body_as_html']

    def body_as_html(self, obj):
        return obj.body[100]
    body_as_html.allow_tags = True



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
                'body_ru',
                'body_en',
            ]
        }),
    ]


admin.site.register(MainPage, MainPageAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(UsefullInformation, InformationAdmin)