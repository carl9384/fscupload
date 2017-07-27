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
        
        #self.halfmap1 = Fscjob.halfmap1file.name.replace(Fscjob.uniquefolder+"/","")
        #self.halfmap2 = Fscjob.halfmap2file.name.replace(Fscjob.uniquefolder+"/","")
        #self.fullmap = Fscjob.fullmapfile.name.replace(Fscjob.uniquefolder+"/","")
        print("full map path is ",self.fullmap)
        self.apix = float(Fscjob.apix)

        if Fscjob.maskfile is not None:
            self.mask = Fscjob.maskfile.name
        self.ThreeDFSC = 'testrun'
        #self.ThreeDFSC = Fscjob.fullmapfile.name.replace(".mrc","").split("/")[-1]
        #self.ThreeDFSC = Fscjob.fullmapfile.name.replace(".mrc","")
        self.dthetaInDegrees = Fscjob.coneangle
        self.histogram = self.ThreeDFSC+"_histogram"
        #self.histogram = os.path.join(settings.MEDIA_ROOT,Fscjob.uniquefolder+"/"+self.ThreeDFSC+"_histogram")
        self.FSCCutoff = Fscjob.fsccutoff
        self.ThresholdForSphericity = Fscjob.sphericitythresh
        self.HighPassFilter = Fscjob.highpassfilter
        self.Skip3DFSCGeneration = "False"

        from pprint import pprint
        pprint(vars(self))



