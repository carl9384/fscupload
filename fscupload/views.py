from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.http import HttpResponse
from django.views.static import serve
from django.conf import settings

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponseRedirect,redirect
import os

# Add an authentication layer to prevent unwanted access to uploaded and processed data.
@login_required
def protected_serve(request, path, document_root=None):
    try:
        pk = path.split("/")[0]
        if int(pk) == request.user.id:
                document_root = settings.MEDIA_ROOT
                sendfile_path = os.path.join('/protected/',path)
                response = HttpResponse()

                if path[-4:] == '.zip':
                    response['Content-Type'] = 'application'
                else:
                    response['Content-Type'] = 'image/png'
                response['X-Accel-Redirect'] = sendfile_path
   
                return response
        return HttpResponseRedirect('/')
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')


# If a user is already logged in and arrives at the login page, redirect them to index.
def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return login(request)
