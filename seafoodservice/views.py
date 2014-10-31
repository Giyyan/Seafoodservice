# -*- coding: utf-8 -*-
from difflib import context_diff
from django.shortcuts import render_to_response
from django.template import RequestContext

from partners.models import Partner
from gallery.models import PhotoGallery
from information.models import News, MainPage

def main(request):
    context = {
        "partners": Partner.objects.all(),
        "slides": PhotoGallery.objects.filter(add_this_photo_to_slide=True),
        "main_page": MainPage.objects.all()[0]
    }
    context.update(set_required_data(request))
    return render_to_response('main.html',
                          context,
                          context_instance=RequestContext(request))

def set_required_data(request):
    context = {
        "last_news": News.objects.all().order_by("-date")[:4],

    }
    return context