from django.urls import path
from userauths.views import signup, login_view, logout_view



app_name = 'userauths'

urlpatterns = [
    path("signup/", signup, name='signup'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
]
