from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from course.models import CourseCategory
from subscription.models import SubscriptionPlanItie
from .models import ICourse, testimonial
from django.contrib import messages
from .models import Contact
from django.http import HttpResponse
from django.views import View
from django.shortcuts import  get_object_or_404
from subscription.models import SubscriptionPlanItie
from userauths.models import Dashboard_User
from django.contrib.auth.models import User

# Create your views here.

login_required(login_url='/userauths/login/')
def itie(request):
    if request.method == 'POST':
        name_ = request.POST.get('name_')
        email_ = request.POST.get('email_')
        mobile_ = request.POST.get('mobile_')
        profession_ = request.POST.get('profession_')
        contact_obj = Contact(name=name_,email=email_,mobile=mobile_,profession=profession_)
        contact_obj.save()
        messages.success(request,'thank you for contacting us')
    courses = ICourse.objects.all()
    testimonials = testimonial.objects.all()
    categories = CourseCategory.objects.all()
    i_plans = SubscriptionPlanItie.objects.filter(active=True)
    user = request.user
    if request.user.is_authenticated:
        auser = User.objects.get(username=user)  
        dash_user = Dashboard_User.objects.get(user_id=auser.id)
        photo = dash_user.photo
        return render(request,'ITIE.html',
                  {'is_itie': True, 
                   'courses':courses , 
                   'testimonials':testimonials, 
                   'categories':categories,
                   'i_plans':i_plans,
                   'photo':photo
                   })
    return render(request,'ITIE.html',
                  {'is_itie': True, 
                   'courses':courses , 
                   'testimonials':testimonials, 
                   'categories':categories,
                   'i_plans':i_plans
                   })

class DownloadFileView(View):
    def get(self,request,pk):
        itie = get_object_or_404(ICourse, pk = pk)
        file_content = itie.brochure.read()
        file_name = itie.brochure.name
        response = HttpResponse(file_content, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response