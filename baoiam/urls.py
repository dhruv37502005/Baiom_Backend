
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from userauths import views
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('userauths/', include('userauths.urls')),
    path('contactus/', include('contactapp.urls')),
    #path('dashboard/', include('dashboard.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)