
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from core.views import maintenance_page, locked_page
from userauths import views
from dashboard import views
from course import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('userauths/', include('userauths.urls')),
    path('contactus/', include('contactapp.urls')),
    path('course/', include('course.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('maintenance/', maintenance_page, name='maintenance'),
    # path('locked/', locked_page, name='locked'),
    # path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    path('blog/', include('blog.urls', namespace='blog')),
    # For social auth

    path('auth/', include('social_django.urls', namespace='social')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)