from celery.decorators import task
from celery.utils.log import get_task_logger

from upload.emails import send_upload_email

logger = get_task_logger(__name__)


@task(name="send_upload_email_task")
def send_upload_email_task(email, message):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent uploadcomplete email")
    return send_upload_email(email, message)


@task(name="sum_two_numbers")
def add(x, y): 
    return x + y 
