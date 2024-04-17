from django.shortcuts import render
from course.models import CourseCategory
from .models import BootCourse, testimonial
from django.views import View
from .models import BootCourse, BootBatch
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact
from .serializers import BootCourseSerializer, TestimonialSerializer, BootBatchSerializer
from rest_framework import generics
from subscription.models import SubscriptionPlanBootcamp
from .models import BootCourse , BootBatch 
from userauths.models import Dashboard_User
from django.contrib.auth.models import User


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

    subscription_plans_bootcamp = SubscriptionPlanBootcamp.objects.filter(active = True)
    courses = BootCourse.objects.all()
    testimonials = testimonial.objects.all()
    categories = CourseCategory.objects.all()
    user = request.user
    if request.user.is_authenticated:
        auser = User.objects.get(username=user)  
        dash_user = Dashboard_User.objects.get(user_id=auser.id)
        photo = dash_user.photo
    return render(request,'wep.html',{'courses':courses , 'testimonials':testimonials, 'categories':categories,'subscription_plans_bootcamp':subscription_plans_bootcamp,'photo':photo})

class DownloadFileView(View):
    def get(self,request, *args, **kwargs):
        bootcamp = get_object_or_404(BootCourse,is_wep_main =True)
        file_content = bootcamp.brochure.read()
        file_name = bootcamp.brochure.name
        response = HttpResponse(file_content, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response


# RestAPI Views Here

class bootcamp_course_list(generics.ListCreateAPIView):
    queryset = BootCourse.objects.all()
    serializer_class = BootCourseSerializer

class bootcamp_course_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BootCourse.objects.all()
    serializer_class = BootCourseSerializer
    lookup_field = 'id'

class testimonial_list(generics.ListCreateAPIView):
    queryset = testimonial.objects.all()
    serializer_class = TestimonialSerializer

class testimonial_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = testimonial.objects.all()
    serializer_class = TestimonialSerializer
    lookup_field = 'id'

class bootbatch_list(generics.ListCreateAPIView):
    queryset = BootBatch.objects.all()
    serializer_class = BootBatchSerializer

class bootbatch_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BootBatch.objects.all()
    serializer_class = BootBatchSerializer
    lookup_field = "id"

    

