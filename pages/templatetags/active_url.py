# -*- coding=utf-8 -*-
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def is_active_url(request, url_name):
    if (url_name is 'home'):
        return "active" if request.path == '/' else ""
    else:
        url = reverse(url_name)
        return "active" if request.path.find(url) + 1 else ""
    print url, request.path