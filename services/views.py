from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def services(request):
    context = {
        "main_services": Service.objects.filter(is_fundamental_service=True),
        "extra_services": Service.objects.filter(is_fundamental_service=False)
    }
    return render_to_response('services.html',
                          context,
                          context_instance=RequestContext(request))

def service_item(request):
    context = {}
    return render_to_response('services_item.html',
                          context,
                          context_instance=RequestContext(request))