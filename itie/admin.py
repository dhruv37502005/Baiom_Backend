from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import ICourse, IBatch
from .models import testimonial
from .models import Contact
class ICourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'status', 'brochure')

class IBatchAdmin(admin.ModelAdmin):
    list_display = ('batch_name', 'course', 'start_date', 'end_date')


admin.site.register(ICourse, ICourseAdmin)
admin.site.register(IBatch, IBatchAdmin)
admin.site.register(testimonial)
admin.site.register(Contact)