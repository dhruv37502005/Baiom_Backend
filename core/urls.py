from django.urls import path
# from course.views import categories
from core.views import index, career, hire_from_us, itie,wep, blog,pap, refer_earn, course, coming_soon, blog_details


app_name = 'core'

urlpatterns = [
    path("", index, name="index"),
    path("career/", career, name="career"),
    path("hire_from_us/", hire_from_us, name="hire_from_us"),
    path("itie/", itie, name="itie"),
    path("wep/", wep, name="wep"),
    path("blog/", blog, name="blog"),
    path("blog_details", blog_details, name="blog_details"),
    path("pap/", pap, name="pap"),
    path("refer_earn/", refer_earn, name="refer_earn"),
    path("coming_soon/", coming_soon, name="coming_soon"),
    path("course/", course, name="course"),
    # path('categories/', categories, name='categories'),
]
