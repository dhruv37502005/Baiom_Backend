from django.contrib import admin
from django.contrib import admin
from . models import Contact
from import_export.admin import ImportExportModelAdmin


class contactadmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['sno','timestamp','name','email','course','phone','content']
    
admin.site.register(Contact,contactadmin)
