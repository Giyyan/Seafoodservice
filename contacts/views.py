from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from information.views import set_required_data

def contacts(request):
    context = dict(contacts=[{
                                 "contact": employee,
                                 "skypes": SkypeName.objects.filter(contact=employee),
                                 "numbers": TelephoneNumber.objects.filter(contact=employee),
                                 "emails": Email.objects.filter(contact=employee)}
                                for employee in Employee.objects.all()],
                   office_contacts=[dict(contact=employee, skypes=SkypeName.objects.filter(contact=employee),
                                         numbers=TelephoneNumber.objects.filter(contact=employee),
                                         emails=Email.objects.filter(contact=employee),
                                         faxs=FaxNumber.objects.filter(contact=employee))
                                    for office in OfficeContact.objects.all()])
    context.update(set_required_data(request))
    return render_to_response('contacts.html',
                          context,
                          context_instance=RequestContext(request))