from django.db import models
from django import conf
from django.utils import timezone
from hashlib import sha3_512


# Create your models here.

from django.db import models


def generate_uniquestring(numchars):

    assert type(numchars) == int
    assert numchars > 0
    assert numchars <21

    hasher = sha3_512()
    hasher.update(str(timezone.now()).encode('utf-8'))
    return hasher.hexdigest()[:numchars]

class Fscjob(models.Model):

    emailaddress = models.EmailField()
    halfmap1file = models.FileField()
    halfmap2file = models.FileField()
    fullmapfile  = models.FileField()
    apix = models.FloatField(default=1.1)
    maskfile = models.FileField()
    coneangle = models.FloatField(default=20.0)
    fsccutoff = models.FloatField(default=0.143)
    sphericitythresh = models.FloatField(default=0.5)
    highpassfilter = models.FloatField(default=150.0)
    uniquefolder = models.CharField(max_length=20,default=generate_uniquestring(20))
    password = models.CharField(max_length=20,default=generate_uniquestring(10))
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)



    #https://stackoverflow.com/questions/8080257/how-to-show-download-link-for-attached-file-in-filefield-in-django-admin
    def file_link(self):
        if self.halfmap1file:
            return "<a href='%s' download>%s</a>" % (self.halfmap1file.name,self.halfmap1file.name)
        else:
            return "No attachment"

    file_link.allow_tags = True

    def file_name(self):

        if self.halfmap1file:
            return self.halfmap1file.name

    def __unicode__(self):
        return self.halfmap1file.file_name

    def get_url(self):
        return self.halfmap1file.url
