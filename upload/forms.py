from django.forms import ModelForm
from django import forms
from upload.models import Fscjob


#class FscjobForm(forms.Form):
#    halfmap1file = forms.FileField(label='Select a file')

class FscjobForm(ModelForm):

    maskfile = forms.FileField(required=False)
    class Meta:
        model = Fscjob
        exclude = ['maskfile']
