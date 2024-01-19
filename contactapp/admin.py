from django.contrib import admin
from django.contrib import admin
from . models import Contact

class contactadmin(admin.ModelAdmin):
    list_display=['sno','timestamp','name','email','course','phone','content']
    
admin.site.register(Contact,contactadmin)
