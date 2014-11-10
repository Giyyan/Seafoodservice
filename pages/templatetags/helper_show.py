from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from information.models import News, UsefullInformation

register = template.Library()


@register.inclusion_tag('show_latest_news.html')
def show(name='news', count_of_latest_news=10):
    url = reverse(name)
    url_item = '{}_item'.format(name,)
    if name == 'news':
        title = _(u"News")
        model = News
    else:
        title = _(u"Useful Information")
        model = UsefullInformation
    objs = model.objects.order_by('-date')[:count_of_latest_news]
    return {'objs': objs, 'title': title, 'url': url, 'url_item': url_item}
