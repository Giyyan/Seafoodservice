from django.conf.urls import patterns, include, url
from django.contrib import admin

import settings

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^$', 'seafoodservice.views.main', name='main'),
    url(r'^contacts$', 'employees.views.contacts', name='contacts'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
)

#services
urlpatterns += patterns('services.views',
    url(r'^services/$', 'services', name='services'),
    url(r'^services/(?P<service_id>\d+)/$', 'service_item', name='servce_item'),
                        )

#news
urlpatterns += patterns('information.views',
    url(r'^news/$', 'news', name='news'),
    url(r'^news/(?P<news_id>\d+)/$', 'news_item', name='news_item'),
    url(r'^usefull-information/$', 'usefull_information', name='usefull_information'),
    url(r'^usefull-information/(?P<information_id>\d+)/$', 'usefull_information_item', name='usefull_information_item'),
                        )

#gallery
urlpatterns += patterns('gallery.views',
    url(r'^gallery/$', 'gallery', name='gallery'),
    url(r'^get_slide_images/$', 'get_slide_images', name='get_slide_images'),
    )

#certificates
urlpatterns += patterns('certificates.views',
    url(r'^certificates/$', 'certificates', name='certificates'),
    url(r'^certificates/(?P<certificate_id>\d+)/$', 'certificate_item', name='certificate_item'),
                        )