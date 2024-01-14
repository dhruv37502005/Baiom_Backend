from django.contrib import admin
from core.models import MaintenancePage

# Register your models here.
class MaintenancePageAdmin(admin.ModelAdmin):
    list_display = ('name','is_enabled','access_code')
admin.site.register(MaintenancePage, MaintenancePageAdmin)