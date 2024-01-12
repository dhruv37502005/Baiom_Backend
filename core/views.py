from django.shortcuts import render
from django.shortcuts import render, redirect

from core.forms import AccessForm


def index(request):
    return render(request, 'index.html',{'is_index_page': True})


def career(request):
    return render(request, 'career.html')

def hire_from_us(request):
    return render(request, 'hire_from_us.html')

def ITIE(request):
    return render(request, 'ITIE.html')

def wep(request):
    return render(request, 'wep.html')

def blog(request):
    return render(request, 'blog.html')


def PAP(request):
    return render(request, 'pap.html')

def earn_refer(request):
    return render(request, 'earn_refer.html')

def maintenance_page(request):
    return render(request, 'maintenance_break.html')

def locked_page(request):
    # form =  AccessForm()
    # return render(request, 'maintenance_locked.html', {'form': form})
    pass