from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string

def send_upload_email(email, message,job):
    c = Context({'email': email, 'message': message, 'job': job})

    email_subject = render_to_string(
        'upload/email/upload_email_subject.txt', c).replace('\n', '')
    email_body = render_to_string('upload/email/upload_email_body.txt', c)

    email = EmailMessage(
        email_subject, email_body, email,
        [settings.DEFAULT_FROM_EMAIL], [],
        headers={'Reply-To': email}
    )
    return email.send(fail_silently=False)


def send_processing_complete_email(job):
    c = Context({'job':job,'site_url':settings.SITE_URL})

    email_subject = render_to_string(
        'upload/email/upload_processing_complete_subject.txt',c).replace('\n','')
    email_body = render_to_string('upload/email/upload_processing_complete_body.txt',c)
    email = EmailMessage(
        email_subject, email_body, job.emailaddress,
        [settings.DEFAULT_FROM_EMAIL],[],
        headers={'Reply-To': job.emailaddress}
    )
    return email.send(fail_silently=False)
