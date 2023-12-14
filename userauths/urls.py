from django.urls import path
from userauths.views import signup



app_name = 'userauth'

urlpatterns = [
    path("signup/", signup,name='signup'),
]
