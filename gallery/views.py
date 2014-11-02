from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import json

from models import PhotoGallery, VideoGallery
from seafoodservice import settings

from information.views import set_required_data

def gallery(request):
    photos = PhotoGallery.objects.filter(add_this_photo_to_gallery=True)
    context = {
        "photos": zip(range(1, len(photos)+1), photos),
        "videos": VideoGallery.objects.all(),
    }
    context.update(set_required_data(request))
    return render_to_response('gallery.html',
                          context,
                          context_instance=RequestContext(request))


def get_slide_images(request):
    context = {
        "slides": [settings.MEDIA_URL+i.photo.name for i in PhotoGallery.objects.filter(add_this_photo_to_slide=True)],
    }
    return HttpResponse(json.dumps(context), mimetype = 'application/json')