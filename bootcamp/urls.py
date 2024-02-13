from django.urls import path
from .views import BootCamp, DownloadFileView

app_name = 'bootcamp'


urlpatterns = [
    path('courses/',BootCamp, name='bootcamp'),
    path('download_file/', DownloadFileView.as_view(), name='download_file'),

]
