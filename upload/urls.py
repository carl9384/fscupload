from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from upload import views as upload_views

app_name = 'upload'
urlpatterns =[

    url(r'^$', upload_views.index, name='index'),
	url(r'^info/$', upload_views.info, name='info'),
    url(r'^submit/$', login_required(upload_views.submit), name='submit'),
    url(r'^uploadcomplete/$',login_required(upload_views.uploadcomplete), name='uploadcomplete'),
    url(r'^jobs/$',login_required(upload_views.fscjobListView.as_view()), name='jobs'),
    url(r'^results/(?P<pk>\d+)$',login_required(upload_views.fscjobDetailView.as_view()),name='results'),
    url(r'^results/$',login_required(upload_views.fscjobListView.as_view()),name='jobs'),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
