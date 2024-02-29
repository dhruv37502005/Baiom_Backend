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
        name_ = request.POST.get('name_')
        email_ = request.POST.get('email_')
        mobile_ = request.POST.get('mobile_')
        profession_ = request.POST.GET('profession')
        contact_obj = Contact(name=name_,email=email_,mobile=mobile_,profession=profession_)
        contact_obj.save()
        messages.success(request,'thank you for contacting us')
    courses = ICourse.objects.all()
    testimonials = testimonial.objects.all()
    categories = CourseCategory.objects.all()
    return render(request,'ITIE.html',{'is_itie': True, 'courses':courses , 'testimonials':testimonials, 'categories':categories})