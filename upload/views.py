from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import os
from upload.models import Fscjob,generate_uniquestring
from upload.forms import FscjobForm
from upload.tasks import process_3DFSC_task
from upload import views as uploadviews
from django.utils import timezone
from hashlib import sha3_512

def generate_uniquestring():
    hasher = sha3_512()
    hasher.update(str(timezone.now()).encode('utf-8'))
    return hasher.hexdigest()[:20]

def list(request):

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
                                highpassfilter = request.POST['highpassfilter']
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
                                highpassfilter = request.POST['highpassfilter']
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
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse(uploadviews.index))

        
        check_delete_folder_path(temp_path)
        return HttpResponseRedirect(reverse(uploadviews.uploadcomplete))
    else:
        form = FscjobForm() # A empty, unbound form

    # Load documents for the list page
    documents = Fscjob.objects.all()

    # Render list page with the documents and the form

    return render(request,'upload/list.html',{'documents': documents,'form':form})
#    return render_to_response(
#        'upload/list.html',
#        {'documents': documents, 'form': form},
#        context_instance=RequestContext(request)
#    )

def index(request):
    return HttpResponseRedirect(reverse(uploadviews.list))

def uploadcomplete(request):
    return render(request,'upload/uploadcomplete.html',{})


def check_delete_folder_path(temp_path):

    if os.path.exists(temp_path):
        if os.listdir(temp_path) == []: 
            os.rmdir(temp_path)
