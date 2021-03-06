from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from hashlib import sha512
from upload.models import Fscjob,generate_uniquestring
from upload.forms import FscjobForm
from upload.tasks import process_3DFSC_task
from upload.tasks import send_upload_email_task

#from sendfile import sendfile

def generate_uniquestring():
    hasher = sha512()
    hasher.update(str(timezone.now()).encode('utf-8'))
    return hasher.hexdigest()[:20]

def submit(request):

    if request.method == 'POST':
        form = FscjobForm(request.POST, request.FILES)
        print("form is ",form)
        if form.is_valid():
            print("VALID")
            num_jobs = Fscjob.objects.filter(user=request.user).count()
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
            uniquefolder = str(request.user.id)+"/%03d/"%num_jobs
            newdoc.uniquefolder = uniquefolder
            newdoc.halfmap1file.name = uniquefolder+newdoc.halfmap1file.name
            newdoc.halfmap2file.name = uniquefolder+newdoc.halfmap2file.name
            newdoc.fullmapfile.name = uniquefolder+newdoc.fullmapfile.name
            if 'maskfile' in request.FILES:
                newdoc.maskfile = request.FILES['maskfile']
                newdoc.maskfile.name = uniquefolder+newdoc.maskfile.name
            
            newdoc.save()
            print("newdoc saved")
            send_upload_email_task.delay(newdoc.id)
            print("email sent")
            process_3DFSC_task.delay(newdoc.id)
            print("process complete")
            return HttpResponseRedirect(reverse('upload:uploadcomplete'))

        else:
        
            form = form
            print("form is ",form)           
            # Redirect to the after POST
           
            return render(request,'upload/submit.html',{'form':form})
    else:
        form = FscjobForm() # A empty, unbound form

    return render(request,'upload/submit.html',{'form':form})

def index(request):
    return render(request,'upload/index.html',{})

def uploadcomplete(request):
    return render(request,'upload/uploadcomplete.html',{"DEFAULT_FROM_EMAIL":settings.DEFAULT_FROM_EMAIL})
	
def info(request):
    return render(request,'upload/info.html',{})
	
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
        #context['histogram_url'] = 
        print("fscjobDetailView context is",context)
        return context

