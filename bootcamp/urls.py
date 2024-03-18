from django.urls import path
from .views import BootCamp, DownloadFileView
from .views import bootcamp_course_list, bootcamp_course_detail, testimonial_list, testimonial_detail

app_name = 'bootcamp'


urlpatterns = [
    path('',BootCamp, name='bootcamp'),
    path('download_file/', DownloadFileView.as_view(), name='download_file'),
    path('bootcamp_course_list/', bootcamp_course_list.as_view(), name='bootcamp_course_list'),
    path('bootcamp_course_detail/<int:id>/', bootcamp_course_detail.as_view(), name='bootcamp_course_detail'),
    path('testimonial_list/', testimonial_list.as_view(), name='testimonial_list'),
    path('testimonial_detail/<int:id>/', testimonial_detail.as_view(), name='testimonial_detail'),

]
