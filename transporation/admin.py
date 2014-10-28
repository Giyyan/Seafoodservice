# coding: utf-8
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from modeltranslation.admin import TranslationAdmin
from mptt.forms import forms
from models import GeograohyTransporation

class MPTTAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MPTTAdminForm, self).__init__(*args, **kwargs)

class GeograohyTransporationAdmin(MPTTModelAdmin, TranslationAdmin):
    list_display = ['title', 'description']
    # , 'point']
    form = MPTTAdminForm

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
                'title',
                'description',
                # 'point'
            ]
        }),
    ]

admin.site.register(GeograohyTransporation, GeograohyTransporationAdmin)