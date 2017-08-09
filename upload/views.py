from django.shortcuts import render

# Create your views here.

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from hashlib import sha3_512
import os
from upload.models import Fscjob,generate_uniquestring
from upload.forms import FscjobForm
from upload.tasks import process_3DFSC_task
from upload.tasks import send_upload_email_task

from sendfile import sendfile

def generate_uniquestring():
    hasher = sha3_512()
    hasher.update(str(timezone.now()).encode('utf-8'))
    return hasher.hexdigest()[:20]

def submit(request):

    if request.method == 'POST':

        form = FscjobForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Fscjob(halfmap1file = request.FILES['halfmap1file'],
                                halfmap2file = request.FILES['halfmap2file'],
                                fullmapfile  = request.FILES['fullmapfile'],
                                jobname = request.POST['jobname'],
                                apix = request.POST['apix'],
                                coneangle = request.POST['coneangle'],
                                fsccutoff = request.POST['fsccutoff'],
                                sphericitythresh = request.POST['sphericitythresh'],
                                highpassfilter = request.POST['highpassfilter'],
                                user = request.user,
                                password = generate_uniquestring()
                                )
                
            if 'maskfile' in request.FILES:
                newdoc.maskfile = request.FILES['maskfile']

            newdoc.emailaddress = request.user.email
            newdoc.uniquefolder = generate_uniquestring()
    
            uniquefolder = newdoc.uniquefolder+"/"
            newdoc.halfmap1file.name = uniquefolder+newdoc.halfmap1file.name
            newdoc.halfmap2file.name = uniquefolder+newdoc.halfmap2file.name
            newdoc.fullmapfile.name = uniquefolder+newdoc.fullmapfile.name
            if 'maskfile' in request.FILES:
                newdoc.maskfile = request.FILES['maskfile']
                newdoc.maskfile.name = uniquefolder+newdoc.maskfile.name
            
            newdoc.save()
            send_upload_email_task.delay(newdoc.id)
            process_3DFSC_task.delay(newdoc.id)
            temp_path = os.path.join(settings.PROJECT_ROOT,newdoc.uniquefolder)

        else:

            form = FscjobForm()
            
            # Redirect to the after POST
            return HttpResponseRedirect(reverse('upload:index'))
        
        return HttpResponseRedirect(reverse('upload:uploadcomplete'))
    else:
        form = FscjobForm() # A empty, unbound form

    # Load documents for the list page
    documents = Fscjob.objects.all()

    # Render list page with the documents and the form

    return render(request,'upload/submit.html',{'documents': documents,'form':form})

def index(request):
    return render(request,'upload/index.html',{})

def uploadcomplete(request):
    return render(request,'upload/uploadcomplete.html',{})


class fscjobListView(ListView):

    model = Fscjob
    context_object_name = 'fscjobs'
    def get_queryset(self):
        return Fscjob.objects.filter(user=self.request.user).order_by('-created_date')
    def get_context_data(self, **kwargs):
        context = super(fscjobListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['SITE_URL'] = settings.SITE_URL
        return context

class fscjobDetailView(DetailView):

    model = Fscjob
    context_object_name = 'fscjob'
    def get_queryset(self):
        return Fscjob.objects.filter(user=self.request.user).order_by('-created_date')
    def get_context_data(self, **kwargs):
        context = super(fscjobDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['SITE_URL'] = settings.SITE_URL
        context['MEDIA_URL'] = settings.MEDIA_URL
        print("fscjobDetailView context is",context)
        return context

from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponse


