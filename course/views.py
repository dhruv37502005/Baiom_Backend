from django.shortcuts import render

# Create your views here.
def webdevelopment(request):
    return render(request,'webdevelopment.html',{'is_webdevelopment_page': True})