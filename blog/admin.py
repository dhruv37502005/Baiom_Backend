from django.contrib import admin
from blog.models import *
from import_export.admin import ImportExportModelAdmin


class BlogCategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name',)

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('title',)

class CommentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass

admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)