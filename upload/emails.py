from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string


def send_upload_email(job):

    c = {'job': job,'site_url':settings.SITE_URL}

    email_subject = render_to_string(
    'upload/email/upload_email_subject.txt', c).replace('\n', '')

    email_body = render_to_string(
    'upload/email/upload_email_body.txt', c)
    email_to = job.emailaddress

    email_message = EmailMessage(
	email_subject,
	email_body,
	email_to,
	[email_to],
	headers={'Reply-To': settings.DEFAULT_FROM_EMAIL}
	)
    return email_message.send(fail_silently=False)
 

def send_processing_complete_email(job):

    c = {'job':job,'site_url':settings.SITE_URL}
    email_subject = render_to_string(
        'upload/email/upload_processing_complete_subject.txt',c).replace('\n','')

    email_body = render_to_string(
    'upload/email/upload_processing_complete_body.txt', c)
    email_to = job.emailaddress

    email_message = EmailMessage(
        email_subject,
        email_body,
        email_to,
        [email_to],
        headers={'Reply-To': settings.DEFAULT_FROM_EMAIL}
        )
    return email_message.send(fail_silently=False)



