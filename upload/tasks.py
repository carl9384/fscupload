from celery.decorators import task
from celery.utils.log import get_task_logger
from upload.emails import send_upload_email
from upload.emails import send_processing_complete_email
from upload.process import process_3DFSC

from upload.models import Fscjob
from time import sleep

logger = get_task_logger(__name__)


@task(name="send_upload_email_task")
def send_upload_email_task(job_id):
    """sends an email when fscjob is uploaded and submitted successfully"""
    job = Fscjob.objects.get(pk=job_id)

    logger.info("Sent processing started email notification")

    return send_upload_email(job)

@task(name="send_processing_complete_email_task")
def send_processing_complete_email_task(job_id):
    job = Fscjob.objects.get(pk=job_id)
    logger.info("Sent processing complete email notification")
    return send_processing_complete_email(job)


@task(name="sum_two_numbers",bind=True)
def add(self,x, y): 
    
    sleep(2)
    return self.request.id

@task(name="process_3DFSC_task",bind=True, queue='gpu')
def process_3DFSC_task(self,job_id):

    job = Fscjob.objects.get(pk=job_id)
    job.task_id = self.request.id
    job.save()
    logger.info("Process_3DFSC task launched")
    return process_3DFSC(job)



