from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from course.models import CourseCategory
from .models import ICourse, testimonial
from django.contrib import messages
from .models import Contact

# Create your views here.

login_required(login_url='/userauths/login/')
def itie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        contact_obj = Contact(name=name,email=email,mobile=mobile)
        contact_obj.save()
        messages.success(request,'thank you for contacting us')
    courses = ICourse.objects.all()
    testimonials = testimonial.objects.all()
    categories = CourseCategory.objects.all()
    return render(request,'ITIE.html',{'is_itie': True, 'courses':courses , 'testimonials':testimonials, 'categories':categories})