from django.urls import path
from dashboard.views import dashboard, update_user_details



app_name = 'dashboard'

urlpatterns = [
    path("dashboard/", dashboard, name='dashboard'),
    path("updateuser/", update_user_details, name='updateuser'),

]
