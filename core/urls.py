from django.urls import path
from core.views import index,career,hire_from_us,itie,wep,blog,pap,refer_earn


app_name = 'core'

urlpatterns = [
    path("", index, name="index"),
    path("career/", career, name="career"),
    path("hire_from_us/", hire_from_us, name="hire_from_us"),
    path("itie/", itie, name="itie"),
    path("wep/", wep, name="wep"),
    path("blog/", blog, name="blog"),
    path("pap/", pap, name="pap"),
    path("refer_earn/", refer_earn, name="refer_earn"),
    
    
]
