

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from course import views
app_name = 'course'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webdevelopment/',views.webdevelopment,name="webdevelopment") ,
    path('dashboard/',views.dashboard_view,name="dashboard") ,
    
]