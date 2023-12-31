from django.shortcuts import render
from django.shortcuts import render, redirect
from userauths.models import Dashboard_User
from django.contrib.auth.models import User , auth

def index(request):
    return render(request, 'index.html',{'is_index_page': True})

def user_ui(request):

    if request.method == 'GET':

      if request.user.is_authenticated:

        username = request.session['username']
        user = User.objects.get(username=username)

        return render(request,'profile.html' , {"user":user})

      else :
        return redirect('core:index')



    if request.method == 'POST':

       return render(request,'profile.html')