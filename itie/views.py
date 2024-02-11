from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ICourse

# Create your views here.

login_required(login_url='/userauths/login/')
def itie(request):
    courses = ICourse.objects.all()
    
    return render(request,'ITIE.html',{'courses':courses})
   