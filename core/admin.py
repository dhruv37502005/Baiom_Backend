from django.contrib import admin
from .models import MaintenancePage

class MaintenancePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_enabled', 'access_code', 'end_time')
    
admin.site.register(MaintenancePage, MaintenancePageAdmin)
