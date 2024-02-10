from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ICourse, IBatch

class ICourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'status', 'brochure')

class IBatchAdmin(admin.ModelAdmin):
    list_display = ('batch_name', 'course', 'start_date', 'end_date')


admin.site.register(ICourse, ICourseAdmin)
admin.site.register(IBatch, IBatchAdmin)