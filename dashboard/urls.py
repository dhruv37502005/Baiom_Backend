from django.urls import path
from .views import *


app_name = 'dashboard'

urlpatterns = [
    
    path('user_ui/<str:username>', user_ui , name='user_ui'),
    path('user_ui/<str:username>/json', user_ui_json , name='user_ui_json'),    
    path('admin_ui/', admin_ui , name='admin_ui'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
    #pass curr_date => purchase
    path('enroll_plan/<str:date><int:course_id>/', enroll_plan, name='enroll_plan'),
    # ************ RestAPI Links for Testing ************
    path('dash_user_api/', dash_user_api.as_view(), name='dash_user_api'),
    path('dash_user_detail/<str:user__username>/', dash_user_detail.as_view(), name='dash_user_detail'),
]