from django import forms
from upload.models import Fscjob
from upload.tasks import send_upload_email_task


#class FscjobForm(forms.Form):
#    halfmap1file = forms.FileField(label='Select a file')

class FscjobForm(forms.ModelForm):

    maskfile = forms.FileField(required=False)
    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)
#    uniquefolder = forms.CharField(widget=forms.HiddenInput(),required=True)
#    password = forms.CharField(widget=forms.HiddenInput(),required=True)


    class Meta:
        model = Fscjob
        exclude = ['maskfile','uniquefolder','password','completefile']



    def send_email(self,job_id):
        print('inside send_email function')
        # try to trick spammers by checking whether the honeypot field is
        # filled in; not super complicated/effective but it works
        if self.cleaned_data['honeypot']:
            return False

        job = Fscjob.objects.get(pk=job_id)

        message = "Hi,\n \
                  Your 3DFSC job %s is now being processed.\n \
                  You will receive an email when it is complete with a download link.\n\n  \
                  Thanks,\n \
                  \n\n \
                  YTZ, PRB, DL" %(job.jobname)

        send_upload_email_task.delay(
            #self.cleaned_data['emailaddress'], self.cleaned_data['message'])
            self.cleaned_data['emailaddress'],message,job_id)

