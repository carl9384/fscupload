from django.conf import settings
import os

# Impedance matching object to convert from Fscjob model instance to parameters for Anisotropy.ThreeDFSC.ThreeDFSC_Start.py

class fscparams:

    def __init__(self):
        pass

    def __init__(self,job):

        self.halfmap1 = os.path.join(settings.MEDIA_ROOT,job.halfmap1file.name)
        self.halfmap2 = os.path.join(settings.MEDIA_ROOT,job.halfmap2file.name)
        self.fullmap =  os.path.join(settings.MEDIA_ROOT,job.fullmapfile.name)
        
        if job.maskfile:
            self.mask = os.path.join(settings.MEDIA_ROOT,job.maskfile.name)
        else:
            self.mask = ''
        self.apix = float(job.apix)
        self.ThreeDFSC = job.jobname
        self.dthetaInDegrees = job.coneangle
        self.histogram = self.ThreeDFSC+"_histogram"
        self.FSCCutoff = job.fsccutoff
        self.ThresholdForSphericity = job.sphericitythresh
        self.HighPassFilter = job.highpassfilter
        self.Skip3DFSCGeneration = "False"




