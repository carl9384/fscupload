from django.shortcuts import render

# Create your views here.

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views.generic.list import ListView

from hashlib import sha3_512
import os
from upload.models import Fscjob,generate_uniquestring
from upload.forms import FscjobForm
from upload.tasks import process_3DFSC_task


def generate_uniquestring():
    hasher = sha3_512()
    hasher.update(str(timezone.now()).encode('utf-8'))
    return hasher.hexdigest()[:20]

def submit(request):

    if request.method == 'POST':

        form = FscjobForm(request.POST, request.FILES)
        if form.is_valid():
            if 'maskfile' in request.FILES:
                newdoc = Fscjob(halfmap1file = request.FILES['halfmap1file'],
                                halfmap2file = request.FILES['halfmap2file'],
                                fullmapfile  = request.FILES['fullmapfile'],
                                maskfile = request.FILES['maskfile'],
                                jobname = request.POST['jobname'],
                                emailaddress = request.POST['emailaddress'],
                                apix = request.POST['apix'],
                                coneangle = request.POST['coneangle'],
                                fsccutoff = request.POST['fsccutoff'],
                                sphericitythresh = request.POST['sphericitythresh'],
                                highpassfilter = request.POST['highpassfilter'],
                                user = request.user,
                                password = generate_uniquestring()
                                )

                newdoc.uniquefolder = generate_uniquestring()
        
                uniquefolder = newdoc.uniquefolder+"/"
                newdoc.halfmap1file.name = uniquefolder+newdoc.halfmap1file.name
                newdoc.halfmap2file.name = uniquefolder+newdoc.halfmap2file.name
                newdoc.fullmapfile.name = uniquefolder+newdoc.fullmapfile.name
                newdoc.maskfile.name = uniquefolder+newdoc.maskfile.name
                
                print('newdoc is',newdoc.halfmap1file.name)
                newdoc.save()
                form.send_email(newdoc.id)
                process_3DFSC_task.delay(newdoc.id)
            else:
                newdoc = Fscjob(halfmap1file = request.FILES['halfmap1file'],
                                halfmap2file = request.FILES['halfmap2file'],
                                fullmapfile  = request.FILES['fullmapfile'],
                                emailaddress = request.POST['emailaddress'],
                                jobname = request.POST['jobname'],
                                apix = request.POST['apix'],
                                coneangle = request.POST['coneangle'],
                                fsccutoff = request.POST['fsccutoff'],
                                sphericitythresh = request.POST['sphericitythresh'],
                                highpassfilter = request.POST['highpassfilter'],
                                user = request.user,
                                password = generate_uniquestring()
                                ) 
                newdoc.uniquefolder = generate_uniquestring()
                uniquefolder = newdoc.uniquefolder+"/"
                newdoc.halfmap1file.name = uniquefolder+newdoc.halfmap1file.name
                newdoc.halfmap2file.name = uniquefolder+newdoc.halfmap2file.name
                newdoc.fullmapfile.name  = uniquefolder+newdoc.fullmapfile.name
                print('newdoc is',newdoc.halfmap1file.name)
                newdoc.save()
                form.send_email(newdoc.id)
                process_3DFSC_task.delay(newdoc.id)
            
            temp_path = os.path.join(settings.PROJECT_ROOT,newdoc.uniquefolder)

        else:

            #newdoc.save()
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
        return Fscjob.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super(fscjobListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['SITE_URL'] = settings.SITE_URL
        context['MEDIA_URL'] = settings.MEDIA_URL
        context['MEDIA_ROOT'] = settings.MEDIA_ROOT
        return context
