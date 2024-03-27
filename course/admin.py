from django.contrib import admin
from .models import Course, CourseCategory, Batch, Resource, CourseCarriculum
from .models import Course ,Testimonial, Contact
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CourseAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('title', 'category','status')
admin.site.register(Course,CourseAdmin)

class CourseCategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(CourseCategory,CourseCategoryAdmin)

class CourseCarriculumAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...
admin.site.register(CourseCarriculum,CourseCarriculumAdmin)

class BatchAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('batch_name',)
admin.site.register(Batch,BatchAdmin)

class ResourceAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('created_at', 'get_course_title')

    def get_course_title(self, obj):
        return obj.course.title if obj.course else ''

    get_course_title.short_description = 'Course Title'

admin.site.register(Resource, ResourceAdmin)

class CourseTestimonialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...
admin.site.register(Testimonial,CourseTestimonialAdmin)

class CourseContactAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...
admin.site.register(Contact,CourseContactAdmin)
