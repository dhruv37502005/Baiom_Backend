from django.contrib import admin
from .models import Course, CourseCategory, Batch, Resource, CourseCarriculum #, Purchase
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','status')
admin.site.register(Course,CourseAdmin)

class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(CourseCategory,CourseCategoryAdmin)

# admin.site.register(Purchase)
admin.site.register(CourseCarriculum)

class BatchAdmin(admin.ModelAdmin):
    list_display = ('batch_name',)
admin.site.register(Batch,BatchAdmin)

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'get_course_title')

    def get_course_title(self, obj):
        return obj.course.title if obj.course else ''

    get_course_title.short_description = 'Course Title'

admin.site.register(Resource, ResourceAdmin)