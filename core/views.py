from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User
from core.forms import AccessForm
from course.models import CourseCategory
from django.contrib.auth import authenticate, login, logout


def index(request):

    try:
        existing_user = User.objects.filter(email=request.user.email).exclude(username=request.user.username).first()
        if existing_user:
            user = User.objects.get(id=request.user.id)
            user.delete()
            messages.error(request, f' Email already exists {existing_user.username}')
            return redirect('userauths:login')
    except:
        print("None")
            
    return render(request, 'index.html',{'is_index_page': True})


def career(request):
    return render(request, 'career.html',{'is_career': True})

def hire_from_us(request):
    return render(request, 'hire_from_us.html',{'is_hire': True})

def itie(request):
    return render(request, 'ITIE.html',{'is_itie': True})

def wep(request):
    return render(request, 'wep.html',{'is_wep': True})

def blog(request):
    return render(request, 'blog.html',{'is_blog': True})

def blog_details(request):
    return render(request, 'blog_details.html', {'is_blog_details': True})


def pap(request):
    return render(request, 'pap.html',{'is_pap': True})

def refer_earn(request):
    return render(request, 'referEarn.html',{'is_refer': True})

def maintenance_page(request):
    return render(request, 'maintenance_break.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')

def locked_page(request):
    # form =  AccessForm()
    # return render(request, 'maintenance_locked.html', {'form': form})
    pass
  

def course(request):
    categories = CourseCategory.objects.all()
    # print(categories)
    return render(request, 'course.html', {'is_courses': True, 'categories': categories})
