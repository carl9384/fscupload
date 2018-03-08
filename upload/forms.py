from django import forms
from upload.models import Fscjob
from upload.tasks import send_upload_email_task

# Based on the instructions at https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/

class FscjobForm(forms.ModelForm):

    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)


    class Meta:
        model = Fscjob
        exclude = ['emailaddress','uniquefolder','password','completefile','user','histogram_file','ftplot_file','plots_file','task_id']
        widgets = { 'apix': forms.TextInput({'size': 10})}

