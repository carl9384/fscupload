from django import forms

from upload.models import Fscjob

class FscjobForm(forms.ModelForm):

    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)
    jobname = forms.CharField(min_length=5,max_length=40, required=True)
    apix = forms.FloatField(max_value=3.0,required=True)

    class Meta:
        model = Fscjob
        exclude = ['emailaddress','uniquefolder','password','completefile','user','histogram_file','ftplot_file','plots_file','task_id']
        widgets = { 'apix': forms.TextInput({'size': 10})}

