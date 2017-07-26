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
def list(request):

    def form_valid(self, form):
            form.send_email()
            return super(FscjobView, self).form_valid(form)


    # Handle file upload
    if request.method == 'POST':
        form = FscjobForm(request.POST, request.FILES)
        if form.is_valid():
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
            else:
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

            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse(uploadviews.list))
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
