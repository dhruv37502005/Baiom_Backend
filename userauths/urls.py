from django.urls import path
from userauths.views import signup,login,contactus


app_name = 'core'

urlpatterns = [
    path("signup/", signup,name='signup'),
    path("login/", login,name='login'),
    path("contactus/", contactus,name='contactus'),
]
