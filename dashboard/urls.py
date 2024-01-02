from django.urls import path
from .views import user_ui, admin_ui


app_name = 'dashboard'

urlpatterns = [
    
    path('user_ui/', user_ui , name='user_ui'),
    path('admin_ui/', admin_ui , name='admin_ui'),
]