from django.shortcuts import render_to_response
from django.template import RequestContext

from seafoodservice.views import set_required_data
from models import Employee

def contacts(request):
    context = {
        'contacts' : Employee.objects.all(),
    }
    context.update(set_required_data(request))
    return render_to_response('contacts.html',
                          context,
                          context_instance=RequestContext(request))