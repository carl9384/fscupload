"""fscupload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from registration.backends.hmac.views import RegistrationView
from fscupload.forms import CustomUserForm
import fscupload.views as fscupload_views


# admin.autodiscover()
from upload import views as uploadviews

urlpatterns = [
    url(r'^accounts/register/$',RegistrationView.as_view(form_class=CustomUserForm),name='registration_register',),

    url(r'^accounts/login/',fscupload_views.custom_login,name='accounts-login'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/password/reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^accounts/password/reset/complete$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/$',auth_views.login,name='login'),
    url(r'^login/$',fscupload_views.custom_login,name='login'),
    url(r'^logout/$', auth_views.logout_then_login,name='logout'),
    url(r'^upload/', include('upload.urls', namespace='upload')),
    url(r'^$', uploadviews.index,name='index'),
    #url(r'^{}(?P<path>.*)$'.format(settings.MEDIA_URL[1:]), fscupload_views.protected_serve,name='protected_serve'),
    url(r'^media/(?P<path>.*)$', fscupload_views.protected_serve,name='protected_serve'),
    url(r'^download_file/(?P<path>.*)$', fscupload_views.protected_download,name='protected_download'),
    #url(r'^<path>$', fscupload_views.protected_serve,name='protected_serve'),
#    url(r'^media/(?P<pk>\d+)/(?P<num_user_jobs>\d+)/(?P<path>.*)$', fscupload_views.protected_serve,{}),
#    r'^results/(?P<pk>\d+)$

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



