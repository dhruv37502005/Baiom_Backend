from django.shortcuts import render
from django.shortcuts import render, redirect
from userauths.models import Dashboard_User
from django.contrib.auth.models import User , auth



def user_ui(request):

    if request.method == 'GET':

      if request.user.is_authenticated:

        username = request.session['username']
        user = User.objects.get(username=username)
        dash_user=Dashboard_User.objects.get(user_id=user.id)


        return render(request,'dashboard.html' , {"user":user})

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



    