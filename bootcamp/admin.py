from django.contrib import admin

from .models import BootCourse, BootBatch
from .models import testimonial
class BootCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'status', 'brochure')

class BootBatcheAdmin(admin.ModelAdmin):
    list_display = ('batch_name', 'course', 'start_date', 'end_date')


admin.site.register(BootCourse, BootCourseAdmin)
admin.site.register(BootBatch, BootBatcheAdmin)
admin.site.register(testimonial)