from django.forms import ModelForm
from django import forms
from upload.models import Fscjob
from upload.tasks import send_upload_email_task


#class FscjobForm(forms.Form):
#    halfmap1file = forms.FileField(label='Select a file')

class FscjobForm(ModelForm):

    maskfile = forms.FileField(required=False)
    class Meta:
        model = Fscjob
        exclude = ['maskfile']



    def send_email(self):
        # try to trick spammers by checking whether the honeypot field is
        # filled in; not super complicated/effective but it works
        if self.cleaned_data['honeypot']:
            return False
        send_feedback_email_task.delay(
            #self.cleaned_data['emailaddress'], self.cleaned_data['message'])
            self.cleaned_data['emailaddress'],'This is a test. Thanks for participating!')

