from django.urls import path
from dashboard.views import dashboard



app_name = 'dashboard'

urlpatterns = [
    path("dashboard/", dashboard, name='dashboard'),

]
