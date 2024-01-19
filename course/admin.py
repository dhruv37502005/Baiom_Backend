from django.contrib import admin
from .models import Course, CourseCategory
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','status')
admin.site.register(Course,CourseAdmin)

class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(CourseCategory,CourseCategoryAdmin)

