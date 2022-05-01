from django.contrib import admin
from job_opening.models import NewJob
# Register your models here.
admin.site.site_header = "Able Jobs Admin"
admin.site.site_title = "Able Jobs Admin Portal"
admin.site.index_title = "Welcome to Able Jobs"
admin.site.register(NewJob)