from django.shortcuts import redirect, render
#from userauths.form import UseRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.contrib.auth.models import User , auth
from .models import Dashboard_User



def signup(request):


    if request.method == 'POST':
      
      if request.POST['username'] and request.POST['email'] and request.POST['password1']and request.POST['password2'] :

          username =  request.POST['username']
          email =  request.POST['email']

          #name =  request.POST['name']
          #dob =  request.POST['dob']
          #gender =  request.POST['gender']
          #address =  request.POST['address']
          #mobile_no = request.POST['mobile']
          password =  request.POST.get('password1')
          password1 =  request.POST.get('password2')

          if password == password1:
              if User.objects.filter(username = username).exists():
                messages.info(request,'username already taken')
                return redirect("userauths:signup")

              elif User.objects.filter(email = email).exists():
                messages.info(request,'email already taken')
                return redirect("userauths:signup")
                
              else :
                user = User.objects.create_user(username=username,password=password,email=email)   
                user.save()
                
                patientnew = Dashboard_User(user=user)
                patientnew.save()
                messages.info(request,'user created sucessfully')
                
              return redirect("userauths:login")

          else:
            messages.info(request,'password not matching, please try again')
            return redirect("userauths:signup")

      else :
        messages.info(request,'Please make sure all required fields are filled out correctly')
        return redirect("userauths:signup") 


    
    else :
      return render(request,'signup.html')

    


def login_view(request):
  

    if request.method == 'POST':

          username =  request.POST.get('username')
          password =  request.POST.get('password')
 
          user = authenticate(username=username,password=password)

          
          print(user)
          if user is not None : 

              if (user.is_superuser==True):
                 auth.login(request, user)
                 return redirect('dashboard:admin_ui')
              else:
                auth.login(request,user)
                request.session['username'] = user.username
                return redirect('dashboard:user_ui')
          else :
             messages.info(request,'invalid credentials')
             return redirect('userauths:login')
   

    else :
      return render(request,'login.html')



def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")

    return redirect("core:index")
