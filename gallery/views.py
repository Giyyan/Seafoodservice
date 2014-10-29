from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import json

from models import PhotoGallery, VideoGallery

def gallery(request):
    # if request.LANGUAGE_CODE=="ru-ru":
    #     videos = VideoGallery.objects.values_list('photo', 'description_ru')
    #     photos = PhotoGallery.objects.values_list('photo', 'description_ru')
    # else:
    #     videos = VideoGallery.objects.values_list('photo', 'description_en')
    #     photos = PhotoGallery.objects.values_list('photo', 'description_ru')
    context = {
        "photos": PhotoGallery.objects.all(),
        "videos": VideoGallery.objects.all(),
    }
    return render_to_response('gallery.html',
                          context,
                          context_instance=RequestContext(request))

from seafoodservice import settings
def get_slide_images(request):
    context = {
        "slides": [settings.MEDIA_URL+i.photo.name for i in PhotoGallery.objects.filter(add_this_photo_to_slide=True)],
    }
    print context
    return HttpResponse(json.dumps(context), mimetype = 'application/json')