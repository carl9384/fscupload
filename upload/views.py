from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import UploadFileForm
#from django.forms import ModelFormWithFileField

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file



from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from upload.models import Fscjob
from upload.forms import FscjobForm
from upload import views as uploadviews
from django.utils.crypto import get_random_string
from django.utils import timezone
from hashlib import sha3_512

def generate_uniquestring():
    hasher = sha3_512()
    hasher.update(str(timezone.now()).encode('utf-8'))
    return hasher.hexdigest()[:20]

def list(request):

    def form_valid(self, form):
            print('form is valid')
            form.send_email()
            return super(FscjobView, self).form_valid(form)


    # Handle file upload
    if request.method == 'POST':
        form = FscjobForm(request.POST, request.FILES)
        if form.is_valid():
            uniquefolder = generate_uniquestring()
            if 'maskfile' in request.FILES:
                newdoc = Fscjob(halfmap1file = request.FILES['halfmap1file'],
                                halfmap2file = request.FILES['halfmap2file'],
                                fullmapfile  = request.FILES['fullmapfile'],
                                maskfile = request.FILES['maskfile'],
                                emailaddress = request.POST['emailaddress'],
                                apix = request.POST['apix'],
                                coneangle = request.POST['coneangle'],
                                fsccutoff = request.POST['fsccutoff'],
                                sphericitythresh = request.POST['sphericitythresh'],
                                highpassfilter = request.POST['highpassfilter']
                                )
                newdoc.halfmap1file.name = uniquefolder+newdoc.halfmap1file.name
                newdoc.halfmap2file.name = uniquefolder+newdoc.halfmap2file.name
                newdoc.maskfile.name = uniquefolder+newdoc.maskfile.name
                
                print('newdic is',newdoc.halfmap1file.name)
                newdoc.save()
                form.send_email()
            else:
                print('form IS valid')
                newdoc = Fscjob(halfmap1file = request.FILES['halfmap1file'],
                                halfmap2file = request.FILES['halfmap2file'],
                                fullmapfile  = request.FILES['fullmapfile'],
                                emailaddress = request.POST['emailaddress'],
                                apix = request.POST['apix'],
                                coneangle = request.POST['coneangle'],
                                fsccutoff = request.POST['fsccutoff'],
                                sphericitythresh = request.POST['sphericitythresh'],
                                highpassfilter = request.POST['highpassfilter']
                                ) 
                newdoc.halfmap1file.name = uniquefolder+newdoc.halfmap1file.name
                newdoc.halfmap2file.name = uniquefolder+newdoc.halfmap2file.name
                print('newdic is',newdoc.halfmap1file.name)
                newdoc.save()
                form.send_email()
        else:

            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse(uploadviews.list))
    else:
        print('form is not valid')
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
