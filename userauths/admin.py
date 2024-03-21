from django.contrib import admin
from userauths.models import Dashboard_User
from import_export.admin import ImportExportModelAdmin

# class DashboardAdmin(ImportExportModelAdmin,admin.ModelAdmin):
#     list_display = ('fname', 'lname','user')
# admin.site.register(Dashboard_User,DashboardAdmin)

admin.site.register(Dashboard_User)
# admin.site.register(Employee)
