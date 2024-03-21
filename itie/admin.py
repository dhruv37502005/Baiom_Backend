from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import ICourse, IBatch
from .models import testimonial
from .models import Contact
from import_export.admin import ImportExportModelAdmin


class ICourseAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('title', 'instructor', 'status', 'brochure')

class IBatchAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('batch_name', 'course', 'start_date', 'end_date')

class testimonialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass

admin.site.register(ICourse, ICourseAdmin)
admin.site.register(IBatch, IBatchAdmin)
admin.site.register(testimonial,testimonialAdmin)
admin.site.register(Contact)