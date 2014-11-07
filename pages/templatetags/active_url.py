# -*- coding=utf-8 -*-
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def is_active_url(context, url_name):
    request = context['request']
    print reverse(url_name)
    print dir(request)
    print request.get_full_path
    print "=" * 80
    if (url_name.find('home')+1):
        return "active" if request.path is '/' else ""
    else:
        url = reverse(url_name)
        return "active" if request.path.find(url) + 1 else ""
