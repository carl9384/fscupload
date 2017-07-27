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
        exclude = ['maskfile','uniquefolder','password']



    def send_email(self,job_id):
        print('inside send_email function')
        # try to trick spammers by checking whether the honeypot field is
        # filled in; not super complicated/effective but it works
        if self.cleaned_data['honeypot']:
            return False
        send_upload_email_task.delay(
            #self.cleaned_data['emailaddress'], self.cleaned_data['message'])
            self.cleaned_data['emailaddress'],'This is a test. Thanks for participating!',job_id)

