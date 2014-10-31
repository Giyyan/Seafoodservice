from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from models import News, UsefullInformation

def news(request):
    context = {
        "news": News.objects.all().order_by("-date"),
        "block_information": UsefullInformation.objects.all().order_by("-date")[:4],
        "title_of_infoblock": _(u"Usefull information"),
    }
    return render_to_response('news.html',
                          context,
                          context_instance=RequestContext(request))

def news_item(request, news_id):
    context = {
        "news": News.objects.get(id=news_id),
        "block_information": UsefullInformation.objects.all().order_by("-date")[:4],
        "title_of_infoblock": _(u"Usefull information"),
    }
    return render_to_response('news_item.html',
                          context,
                          context_instance=RequestContext(request))

def usefull_information(request):
    context = {
        "news": UsefullInformation.objects.all().order_by("-date"),
        "last_news": News.objects.all().order_by("-date")[:4],
        "title_of_infoblock": _(u"News"),
        }
    return render_to_response('usefull_information.html',
                          context,
                          context_instance=RequestContext(request))

def usefull_information_item(request, information_id):
    context = {
        "news": UsefullInformation.objects.get(id=information_id),
        "last_news": News.objects.all().order_by("-date")[:4],
        "title_of_infoblock": _(u"News"),
    }
    return render_to_response('usefull_information_item.html',
                          context,
                          context_instance=RequestContext(request))