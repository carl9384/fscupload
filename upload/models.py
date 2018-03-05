from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from hashlib import sha512
from celery.result import AsyncResult

# Create your models here.

def generate_uniquestring(numchars):

    assert type(numchars) == int
    assert numchars > 0
    assert numchars <21

    hasher = sha512()
    hasher.update(str(timezone.now()).encode('utf-8'))
    return hasher.hexdigest()[-numchars:]

class Fscjob(models.Model):

    emailaddress = models.EmailField(verbose_name="Email Address")
    jobname = models.CharField(max_length=15,default="3dfsc_run",verbose_name="Job Name")
    halfmap1file = models.FileField(verbose_name="Half-map 1 file")
    halfmap2file = models.FileField(verbose_name="Half-map 2 file")
    fullmapfile  = models.FileField(verbose_name="Full map file")
    apix = models.FloatField(default=1.1,verbose_name="Pixel Size (Angstrom)")
    maskfile = models.FileField(verbose_name="Mask file",blank=True)
    coneangle = models.FloatField(default=20.0,verbose_name="Cone angle")
    fsccutoff = models.FloatField(default=0.143,verbose_name="FSC Cutoff")
    sphericitythresh = models.FloatField(default=0.5,verbose_name="Sphericity Threshold")
    highpassfilter = models.FloatField(default=150.0,verbose_name="High-pass filter (Angstrom)")
    uniquefolder = models.CharField(max_length=20,default='uniquefolder',verbose_name="Unique folder name")
    password = models.CharField(max_length=20,default='defaultpassword',verbose_name="Password")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Date created")
    modified_date = models.DateTimeField(auto_now=True,verbose_name="Date last modified")
    completefile = models.FileField(verbose_name="Zipped results file")
    histogram_file = models.FileField(verbose_name="Histogram png file",null=True)
    ftplot_file = models.FileField(verbose_name="FTPlot jpg file",null=True)
    plots_file = models.FileField(verbose_name="Plots jpg file",null=True)
    
    user = models.ForeignKey(User)

    task_id = models.CharField(max_length=36,default='',null=True,verbose_name="Task ID")



    #https://stackoverflow.com/questions/8080257/how-to-show-download-link-for-attached-file-in-filefield-in-django-admin


#    def file_link(self):
#        if self.halfmap1file:
#            return "<a href='%s' download>%s</a>" % (self.halfmap1file.name,self.halfmap1file.name)
#        else:
#            return "No attachment"
#
#    file_link.allow_tags = True

    def halfmap1_name(self):
        if self.halfmap1file:
            return self.halfmap1file.name.split("/")[-1:]


    def halfmap2_name(self):
        if self.halfmap2file:
            return self.halfmap2file.name.split("/")[-1:]

    def completefile_name(self):
        if self.completefile:
            return self.completefile.name.split("/")[-1:]
        else:
            return 'Job not completed'
    def __unicode__(self):
        return self.halfmap1file.name.split("/")[-1:]

    def get_url(self):
        return self.halfmap1file.url

    def to_link(filename):
        return "<a href='%s' download>%s</a>" % (filename,filename)

    @property
    def status(self):
        return AsyncResult(self.task_id).status

