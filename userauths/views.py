from django.shortcuts import render
# from userauths.forms import Useregisterform
from userauths.form import Useregisterform


def signup(request):
    if request.method=='POST':
        print("user registered successfully")
    else:
        print("user canot be register")
    form=Useregisterform()
    context={
        'form':form,
    }
    return render(request,'accounts/signup.html',context)

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def contactus(request):
    return render(request, 'contact-page/index.html')