from celery.decorators import task
from celery.utils.log import get_task_logger
from django.conf import settings
import os
from ThreeDFSCprog import ThreeDFSC_Start
from upload.emails import send_upload_email
from upload.models import Fscjob
from upload.fscparams import fscparams
from upload.compress import compress_files

logger = get_task_logger(__name__)


@task(name="send_upload_email_task")
def send_upload_email_task(email, message,job_id):
    """sends an email when feedback form is filled successfully"""
    job = Fscjob.objects.get(pk=job_id)

    logger.info("Sent processing started email")

    return send_upload_email(email, message)


@task(name="sum_two_numbers")
def add(x, y): 
    return x + y 

@task(name="run_ThreeDFSC_job")
def process_3DFSC(job_id):

    job = Fscjob.objects.get(pk=job_id)
    print("CWD is ",os.getcwd())
    directory = job.uniquefolder
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(settings.MEDIA_ROOT+"/"+job.uniquefolder)
    print("CWD is now",os.getcwd())
    options = fscparams(job)
    logger.info("Process_3DFSC task launched")
    ThreeDFSC_Start.execute(options)
    globdirectory = settings.MEDIA_ROOT+"/"+job.uniquefolder+"/"
    print("Compress contents of directory ",globdirectory)
    compress_files(globdirectory+"**",globdirectory+options.ThreeDFSC+".zip",job.password,1)



