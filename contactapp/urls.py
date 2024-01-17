from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from contactapp import views
app_name = 'contactapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactus/',views.contactus,name="contactus"),
]