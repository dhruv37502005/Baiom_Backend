from django.contrib import admin
from userauths.models import Dashboard_User

# class DashboardAdmin(admin.ModelAdmin):
#     list_display = ('fname', 'lname',)
# admin.site.register(DashboardAdmin)

admin.site.register(Dashboard_User)
# admin.site.register(Employee)
