from django.conf.urls import include, url
from upload import views as uploadviews
from django.contrib import admin

urlpatterns =[

    url(r'^$', uploadviews.index, name='index'),
    url(r'^list/$', uploadviews.list, name='list'),
    url(r'^uploadcomplete/$',uploadviews.uploadcomplete, name='uploadcomplete'),
    url(r'^admin/', include(admin.site.urls),name='uploadadmin'),
    ]


    #('upload.views',
    #url(r'^$', 'list', name='list'),
    #    url(r'^list/$', 'list', name='list'),
    #    )
