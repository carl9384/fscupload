from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from upload import views as uploadviews
from django.contrib import admin

urlpatterns =[

    url(r'^$', uploadviews.index, name='index'),
    url(r'^list/$', uploadviews.list, name='list'),
    url(r'^uploadcomplete/$',uploadviews.uploadcomplete, name='uploadcomplete'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    #('upload.views',
    #url(r'^$', 'list', name='list'),
    #    url(r'^list/$', 'list', name='list'),
    #    )
