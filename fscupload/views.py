from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponseRedirect
from upload.models import Fscjob

@login_required
def protected_serve(request, path, document_root=None):
    try:
        objs = Fscjob.objects.filter(user=request.user.id)
        uniquefolders = [obj.uniquefolder for obj in objs]
        for folder in uniquefolders:
            if folder in path:
                document_root = settings.MEDIA_URL[1:]
                return serve(request,path,document_root)
        return HttpResponseRedirect('/')
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')



