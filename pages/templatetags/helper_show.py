from django import template
from django.core.urlresolvers import reverse
from django.template import Context
from django.utils.translation import ugettext_lazy as _

from information.models import News, UsefullInformation

register = template.Library()



def show(name, count_of_latest_news):
    objs = []
    title = ''
    url = url_item = ''
    print "'"+name+"'", type(name)
    if(name == 'news'):
        title = _(u"News")
        objs = News.objects.order_by('-date')[:count_of_latest_news].values('id','title', 'date')
        url = reverse('news')
        url_item = 'news_item'
    elif(name is u'uinfo'):
        title = _(u"Useful Information")
        objs = UsefullInformation.objects.order_by('-date')[:count_of_latest_news].values('id','title')
        url = reverse('usefull_information')
        url_item = 'usefull_information_item'
    print objs, title, url
    return {'objs': objs, 'title': title, 'url': url, 'url_item':url_item}

register.inclusion_tag('show_latest_news.html')(show)