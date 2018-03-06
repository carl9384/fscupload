from django.contrib import admin
from upload.models import Fscjob


# Register your models here.

@admin.register(Fscjob)
class FscjobAdmin(admin.ModelAdmin):
    list_display = ['jobname','status','halfmap1_name','halfmap2_name','completefile_name','created_date']
    readonly_fields=('password','uniquefolder','apix','coneangle','fsccutoff','sphericitythresh','highpassfilter','halfmap1file','halfmap2file','fullmapfile','maskfile','emailaddress','completefile','jobname','user','task_id','status')
    fields = ('jobname','status','task_id','user','emailaddress','completefile','password','halfmap1file','halfmap2file','maskfile','apix','coneangle','fsccutoff','sphericitythresh','highpassfilter')

