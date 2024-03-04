from django.shortcuts import render

from course.models import CourseCategory
from .models import BootCourse, testimonial
from django.views import View
from .models import BootCourse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact
# Create your views here.
def BootCamp(request):
    if request.method == 'POST':
        name_ = request.POST.get('name_')
        email_ = request.POST.get('email_')
        mobile_ = request.POST.get('mobile_')
        profession_ = request.POST.get('profession_')
        contact_obj = Contact(name=name_,email=email_,mobile=mobile_,profession=profession_)
        contact_obj.save()
        messages.success(request,'thank you for contacting us')
    courses = BootCourse.objects.all()
    testimonials = testimonial.objects.all()
    categories = CourseCategory.objects.all()
    return render(request,'wep.html',{'courses':courses , 'testimonials':testimonials, 'categories':categories})


class DownloadFileView(View):
    def get(self,request, *args, **kwargs):
        bootcamp = get_object_or_404(BootCourse,is_wep_main =True)
        file_content = bootcamp.brochure.read()
        file_name = bootcamp.brochure.name
        response = HttpResponse(file_content, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'

        return response

