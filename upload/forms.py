from django import forms
from upload.models import Fscjob
from upload.tasks import send_upload_email_task

# Based on the instructions at https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/

class FscjobForm(forms.ModelForm):

    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)


    class Meta:
        model = Fscjob
        exclude = ['emailaddress','uniquefolder','password','completefile','user']
        widgets = { 'apix': forms.TextInput({'size': 10})}


    def send_email2(self,job_id):
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
            self.cleaned_data['emailaddress'],message,job_id)

