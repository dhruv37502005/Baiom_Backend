from django.contrib import admin
from .models import MaintenancePage, GetInTouch
from import_export.admin import ImportExportModelAdmin


class MaintenancePageAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name', 'is_enabled', 'access_code', 'end_time')
    
admin.site.register(MaintenancePage, MaintenancePageAdmin)
admin.site.register(GetInTouch)
