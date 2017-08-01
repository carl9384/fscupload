from django.conf import settings
import os
from Anisotropy.ThreeDFSC.ThreeDFSC_Start import execute
from upload.compress import compress_files
from upload.fscparams import fscparams
from upload.emails import send_processing_complete_email

def process_3DFSC(job):

    os.chdir(settings.MEDIA_ROOT+"/"+job.uniquefolder)
    options = fscparams(job)
    execute(options)
    globdirectory = settings.MEDIA_ROOT+"/"+job.uniquefolder+"/"
    print("Compress contents of directory ",globdirectory)
    compress_files(globdirectory+"**",globdirectory+options.ThreeDFSC+".zip",job.password,1)
    job.completefile = job.uniquefolder+"/"+options.ThreeDFSC+".zip"
    job.save()

    send_processing_complete_email(job)
    return


