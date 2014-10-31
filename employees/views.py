from django.shortcuts import render_to_response
from django.template import RequestContext

def contacts(request):
    context = {}
    return render_to_response('contacts.html',
                          context,
                          context_instance=RequestContext(request))