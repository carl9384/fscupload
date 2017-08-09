from django.conf import settings
import os
from upload.models import Fscjob

class fscparams:

    def __init__(self):
        pass

    def __init__(self,Fscjob):

        self.halfmap1 = os.path.join(settings.MEDIA_ROOT,Fscjob.halfmap1file.name)
        self.halfmap2 = os.path.join(settings.MEDIA_ROOT,Fscjob.halfmap2file.name)
        self.fullmap =  os.path.join(settings.MEDIA_ROOT,Fscjob.fullmapfile.name)
        
        if Fscjob.maskfile:
            self.mask = os.path.join(settings.MEDIA_ROOT,Fscjob.maskfile.name)
        else:
            self.mask = ''
        self.apix = float(Fscjob.apix)
        self.ThreeDFSC = Fscjob.jobname
        self.dthetaInDegrees = Fscjob.coneangle
        self.histogram = self.ThreeDFSC+"_histogram"
        self.FSCCutoff = Fscjob.fsccutoff
        self.ThresholdForSphericity = Fscjob.sphericitythresh
        self.HighPassFilter = Fscjob.highpassfilter
        self.Skip3DFSCGeneration = "False"




