from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fscupload.settings')


# we need these paths if we are using the gpu version of fscupload
if settings.NUMBAPRO_LIBDEVICE:
    os.environ['NUMBAPRO_LIBDEVICE'] = settings.NUMBAPRO_LIBDEVICE

if settings.NUMBAPRO_NVVM:
    os.environ['NUMBAPRO_NVVM'] = settings.NUMBAPRO_NVVM


app = Celery('fscupload')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
