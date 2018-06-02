from django import forms
from django.core.validators import RegexValidator

from upload.models import Fscjob

no_space_validator = RegexValidator(r'^[^\s]+$',message='No spaces allowed',code='invalid_username')


class FscjobForm(forms.ModelForm):
    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)
    jobname = forms.CharField(min_length=5,max_length=40, required=True,validators=[no_space_validator])
    apix = forms.FloatField(min_value=0.00001,max_value=100.0,required=True)

    class Meta:
        model = Fscjob
        exclude = ['emailaddress','uniquefolder','password','completefile','user','histogram_file','ftplot_file','plots_file','task_id']
        widgets = { 'apix': forms.TextInput({'size': 10})}

