from django.contrib import admin

from . models import DashboardUser
class dashboardadmin(admin.ModelAdmin):
    list_display=['fname','lname','mname','username','mobilenumber', 'email','bio','photo','collegename','graduation_year','current_designation']
admin.site.register(DashboardUser,dashboardadmin)

# Register your models here.


# Register your models here.


# Register your models here.
