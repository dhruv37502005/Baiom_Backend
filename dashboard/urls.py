from django.urls import path
from .views import user_ui, enroll_course, admin_ui, enroll_plan


app_name = 'dashboard'

urlpatterns = [
    
    path('user_ui/', user_ui , name='user_ui'),
    path('admin_ui/', admin_ui , name='admin_ui'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
    #pass curr_date => purchase
    path('enroll_plan/<str:date><int:course_id>/', enroll_plan, name='enroll_plan'),
]