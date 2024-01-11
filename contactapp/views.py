from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import contact


def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        message = request.POST.get('msg')
        course = request.POST.get('course')
        if name != "" and email != "" and phone != "" and message != "" and course != "Courses":
            contact_obj = contact(name=name, email=email, phone=phone, content=message)
            contact_obj.save()
            messages.success(request, "Thank You for contact us")
            redirect("contactapp:contactus")

        else:
            redirect("contactapp:contactus")
            messages.error(request, "All fields are required")

    return render(request, 'contact-us.html', {'is_contactus_page': True})
