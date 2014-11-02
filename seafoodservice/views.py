# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from partners.models import Partner
from gallery.models import PhotoGallery
from information.models import News, MainPage

def main(request):
    context = {
        "partners": Partner.objects.all(),
        "slides": PhotoGallery.objects.filter(add_this_photo_to_slide=True),
        "last_news": News.objects.all().order_by("-date")[:4],
        "main_page": MainPage.objects.all()[0]
    }
    return render_to_response('main.html',
                          context,
                          context_instance=RequestContext(request))


