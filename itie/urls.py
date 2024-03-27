from django.urls import path, include
from .views import itie
from .views import DownloadFileView

app_name = 'itie'


urlpatterns = [
    path("", itie, name="itie"),
    path("download_file/<int:pk>/", DownloadFileView.as_view(), name='download_file'),

]
