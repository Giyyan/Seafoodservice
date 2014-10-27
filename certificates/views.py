from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Certificate

def certificates(request):
    list_certificates = Certificate.objects.all()
    paginator = Paginator(list_certificates,6)
    page = request.GET.get('page')
    try:
        list_certificates = paginator.page(page)
    except PageNotAnInteger:
        list_certificates = paginator.page(1)
    except EmptyPage:
        list_certificates = paginator.page(paginator.num_pages)
    return render_to_response('certificates.html', {"certificates" : list_certificates},
                              context_instance=RequestContext(request))

def certificate_item(request, certificate_id):
    context = {}
    return render_to_response('certificate_item.html',
                          context,
                          context_instance=RequestContext(request))


