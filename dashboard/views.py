from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from course.models import Course
from userauths.models import Dashboard_User
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/userauths/login/')
def user_ui(request):
    if request.method == 'GET':
      auser = request.user
      if request.user.is_authenticated:
        if auser.is_staff==True:
          return redirect('/admin')
        else:
          username = request.session['username']
          user = User.objects.get(username=username)
          dash_user=Dashboard_User.objects.get(user_id=user.id)
          # all_courses = Course.objects.all()
          enrolled_courses = dash_user.enrolled_courses.filter(status='active')
          return render(request, 'dashboard.html', {"user": user, "dash_user": dash_user, 'enrolled_courses': enrolled_courses})
      else :
        return redirect('userauths:login')
    if request.method == 'POST':
       return render(request,'profile.html')
    

# def admin_ui(request):
#     if request.method == 'GET':
#       if request.user.is_authenticated:
#         auser = request.user
#         if auser.is_staff==True:
#           return redirect('core:index')
#         else:
#           return redirect('/admin')
#       else :
#         return redirect('core:index')

@login_required(login_url='/userauths/login/')
def enroll_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)    
    dashboard_user, created = Dashboard_User.objects.get_or_create(user=request.user)
    dashboard_user.enrolled_courses.add(course)
    # messages.success(request, f"You have successfully enrolled in {course.title}.")
    return redirect('dashboard:user_ui')
    