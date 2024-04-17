from django.shortcuts import render, redirect
from django.contrib import messages
from course.models import CourseCategory
from .models import Contact
from userauths.models import Dashboard_User
from django.contrib.auth.models import User

def contactus(request):
    categories = CourseCategory.objects.all()
    user = request.user
    if request.user.is_authenticated:
        auser = User.objects.get(username=user)  
        dash_user = Dashboard_User.objects.get(user_id=auser.id)
        photo = dash_user.photo
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        message = request.POST.get('msg')
        course = request.POST.get('course')

        if name and email and phone and message and course != "Courses":
            contact_obj = Contact(name=name, email=email, phone=phone, course=course, content=message)
            contact_obj.save()
            messages.success(request, "Thank you for contacting us!")
            return redirect("contactapp:contactus")

        else:
            messages.error(request, "All fields are required")
            return redirect("contactapp:contactus")

    return render(request, 'contact-us.html', {'is_contactus_page': True,'categories':categories,'photo':photo})
