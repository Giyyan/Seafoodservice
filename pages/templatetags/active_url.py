# -*- coding=utf-8 -*-
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def is_active_url(context, url_name):
    request = context['request']
    return 'active' \
        if reverse(url_name) == request.get_full_path() else ''
