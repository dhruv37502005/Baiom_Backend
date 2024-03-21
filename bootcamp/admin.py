from django.contrib import admin
from .models import Contact
from .models import BootCourse, BootBatch
from .models import testimonial
from import_export.admin import ImportExportModelAdmin


class BootCourseAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('title', 'instructor', 'status', 'brochure')

class BootBatcheAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('batch_name', 'course', 'start_date', 'end_date')

class testimonialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass

class ContactAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass


admin.site.register(BootCourse, BootCourseAdmin)
admin.site.register(BootBatch, BootBatcheAdmin)
admin.site.register(testimonial,testimonialAdmin)
admin.site.register(Contact,ContactAdmin)