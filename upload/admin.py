from django.contrib import admin
from upload.models import Fscjob


# Register your models here.

@admin.register(Fscjob)
class FscjobAdmin(admin.ModelAdmin):
    list_display = ['file_name','get_url','created_date']
    readonly_fields=('password','uniquefolder','apix','coneangle','fsccutoff','sphericitythresh','highpassfilter','halfmap1file','halfmap2file','fullmapfile','maskfile')
