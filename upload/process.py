from django.conf import settings
import os
from Anisotropy.ThreeDFSC.ThreeDFSC_Start import execute
from upload.compress import compress_files
from upload.fscparams import fscparams
from upload.emails import send_processing_complete_email

def process_3DFSC(job):

    filepath,filename = os.path.split(job.fullmapfile.name)
    filepath = filepath+"/"
    os.chdir(settings.MEDIA_ROOT+filepath)
    options = fscparams(job)

    execute(options)
    globdirectory = settings.MEDIA_ROOT+filepath+"/"
    compress_files(globdirectory+"**",globdirectory+options.ThreeDFSC+".zip",job.password,1)
    job.completefile = filepath+options.ThreeDFSC+".zip"
    job.save()

    send_processing_complete_email(job)
    return


