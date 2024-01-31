from django.shortcuts import render
from course.models import Course
from course.models import CourseCategory
from django.shortcuts import render, get_object_or_404


# Create your views here.
def itie(request,id):
    category = get_object_or_404(CourseCategory ,category_id = id)
    courses = Course.objects.filter(category=category, status='active', itie='True')
    categories = CourseCategory.objects.filter(is_itie ='True')
