from django.contrib import admin

from .models import Course

# Register your models here.

# admin.site.register(Course)
# admin.site.register(Author)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass