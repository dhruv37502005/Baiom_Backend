from django.shortcuts import render, redirect
from  .forms import UserUpdateForm
from django.contrib import messages
from . models import DashboardUser

def dashboard(request):
    return render(request, 'dashboard.html')

def update_user_details(request):
    if request.method=="POST":
        form  = UserUpdateForm(request.POST, instance =  request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "SUccess")
            return redirect(dashboard)
    else:
        form = UserUpdateForm()
    
    return render(request, "dashboard222.html",{'form':form})
        

# Create your views here.
