from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from upload import views as uploadviews
from django.contrib import admin
from django.contrib.auth.decorators import login_required

urlpatterns =[

    url(r'^$', uploadviews.index, name='index'),
    url(r'^submit/$', login_required(uploadviews.submit), name='submit'),
    url(r'^uploadcomplete/$',login_required(uploadviews.uploadcomplete), name='uploadcomplete'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

