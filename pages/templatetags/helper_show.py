from django import template
from django.core.urlresolvers import reverse
from django.template import Context
from django.utils.translation import ugettext_lazy as _

from information.models import News, UsefullInformation

register = template.Library()


@register.simple_tag(takes_context=True)
def show(context, name, count_of_latest_news):
    objs = []
    title = ''
    url = ''
    if(name is u'news'):
        title = _(u"News")
        objs = News.objects.order_by('-date')[:count_of_latest_news].values_list('id','title', 'date')
        url = reverse('news')
    elif(name is u'uinfo'):
        title = _(u"Useful Information")
        objs = UsefullInformation.objects.order_by('-date')[:count_of_latest_news].values_list('id','title')
        url = reverse('usefull_information')
    t = template.loader.get_template('show_latest_news.html')

    return t.render(Context({'objs': objs,
                             'title': title,
                             'url': url},
                            autoescape=context.autoescape))