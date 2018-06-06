from django import forms
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator

from upload.models import Fscjob

no_space_validator = RegexValidator(r'^[^\s]+$',message='No spaces allowed',code='invalid_username')
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
fileextension = FileExtensionValidator(['mrc','map'],message='Only .mrc and .map files can be processed. Please convert your maps to those format.')

class FscjobForm(forms.ModelForm):
    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)
    jobname = forms.CharField(min_length=5,max_length=40, required=True,validators=[alphanumeric])
    apix = forms.FloatField(min_value=0.00001,max_value=100.0,required=True)
    halfmap1file = forms.FileField(required=True,validators=[fileextension])


    class Meta:
        model = Fscjob
        exclude = ['emailaddress','uniquefolder','password','completefile','user','histogram_file','ftplot_file','plots_file','task_id']
        widgets = { 'apix': forms.TextInput({'size': 10})}

