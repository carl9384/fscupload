from django.test import TestCase

# Create your tests here.

import upload.tasks as tasks
import upload.emails as emails
from django.core.mail import EmailMessage
