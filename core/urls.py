from django.urls import path
from core.views import index,career,hire_from_us,ITIE,wep,blog,PAP,earn_refer


app_name = 'core'

urlpatterns = [
    path("", index, name="index"),
    path("career/", career, name="career"),
    path("hire/", hire_from_us, name="hire"),
    path("itie/", ITIE, name="itie"),
    path("wep/", wep, name="wep"),
    path("blog/", blog, name="blog"),
    path("pap/", PAP, name="pap"),
    path("earnandrefer/", earn_refer, name="earn"),
    
    
]
