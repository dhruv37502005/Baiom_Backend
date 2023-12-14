from django.contrib import admin
from django.contrib import admin
from . models import contact
class contactadmin(admin.ModelAdmin):
    list_display=['sno','name','email','phone','content']
admin.site.register(contact,contactadmin)

# Register your models here.


# Register your models here.
