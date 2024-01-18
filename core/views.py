from django.shortcuts import render
from django.shortcuts import render, redirect

from core.forms import AccessForm
from course.models import CourseCategory


def index(request):
    return render(request, 'index.html',{'is_index_page': True})


def career(request):
    return render(request, 'career.html')

def hire_from_us(request):
    return render(request, 'hire_from_us.html')

def itie(request):
    return render(request, 'ITIE.html')

def wep(request):
    return render(request, 'wep.html')

def blog(request):
    return render(request, 'blog.html')


def pap(request):
    return render(request, 'pap.html')

def refer_earn(request):
    return render(request, 'referEarn.html')

def maintenance_page(request):
    return render(request, 'maintenance_break.html')

def locked_page(request):
    # form =  AccessForm()
    # return render(request, 'maintenance_locked.html', {'form': form})
    pass
  

def course(request):
    categories = CourseCategory.objects.all()
    # print(categories)
    return render(request, 'course.html', {'is_courses': True, 'categories': categories})
