from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from course import views


app_name = 'course'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('webdevelopment/',views.webdevelopment,name="webdevelopment"),
    # path('dataanalyst/',views.dataanalyst,name="dataanalyst"),
    # path('datascience/',views.datascience,name="datascience"),
    # path('contentwriting/',views.contentwriting,name="contentwriting"),
    # path('graphicdesigning/',views.graphicdesigning,name="graphicdesigning"),
    # path('seomarketing/',views.seomarketing,name="seomarketing"),
    # path('digitalmarketing/',views.digitalmarketing,name="digitalmarketing"),
    # path('projectmanagement/',views.projectmanagement,name="projectmanagement"),
    # path('humanresource/',views.humanresource,name="humanresource"),
    # path('corporatelaw/',views.corporatelaw,name="corporatelaw"),
    # path('enterpreneurship/',views.enterpreneurship,name="enterpreneurship"),
    # path('webdevelopment/',views.webdevelopment,name="webdevelopment"),
    
    # path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_courses, name='category_courses'),




]