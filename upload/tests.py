from django.test import TestCase

# Create your tests here.

import upload.tasks as tasks
import upload.emails as emails
from django.core.mail import EmailMessage

print("Send email from Django EmailMessage at command line")
job_id = 36

email_subject = 'test subject'
email_body = 'test email body'
email_to = 'cnegro@nysbc.org'
email_from = 'deonnysbc@gmail.com'
email_test = EmailMessage(
    email_subject,
    email_body,
    email_to,
    [email_to],
    headers={'Reply-To':email_from}
    )

print(email_test.send(fail_silently=False))


print("Send email from upload.emails")

emails.send_upload_email(job_id)
