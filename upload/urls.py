from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from upload import views as uploadviews

app_name = 'upload'
urlpatterns =[

    url(r'^$', uploadviews.index, name='index'),
    url(r'^submit/$', login_required(uploadviews.submit), name='submit'),
    url(r'^uploadcomplete/$',login_required(uploadviews.uploadcomplete), name='uploadcomplete'),
    url(r'^jobs/$',login_required(uploadviews.fscjobListView.as_view()), name='jobs'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

