from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from course import views
from .views import DownloadFileView


app_name = 'course'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/<int:category_id>/', views.category_courses, name='category_courses'),
    path('categories/<int:category_id>/json', views.category_courses_json, name='category_courses_json'),
    path('download_file/<int:file_id>/', DownloadFileView.as_view(), name='download_file'),
    path('course_contact/', views.course_contact, name='course_contact')




]