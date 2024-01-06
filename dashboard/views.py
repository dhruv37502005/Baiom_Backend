from django.shortcuts import render
from django.shortcuts import render, redirect
from course.models import Course
from userauths.models import Dashboard_User
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required


@login_required(login_url='/userauths/login/')
def user_ui(request):
    if request.method == 'GET':
      if request.user.is_authenticated:
        username = request.session['username']
        user = User.objects.get(username=username)
        dash_user=Dashboard_User.objects.get(user_id=user.id)
        all_courses = Course.objects.all()
        return render(request, 'dashboard.html', {"user": user, "dash_user": dash_user, 'all_courses': all_courses})
      else :
        return redirect('userauths:login')
    if request.method == 'POST':
       return render(request,'profile.html')
    

def admin_ui(request):
    if request.method == 'GET':
      if request.user.is_authenticated:
        auser = request.user
        return redirect('/admin')
      else :
        return redirect('core:index')



    