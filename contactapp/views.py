from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contactus(request):
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

    return render(request, 'contact-us.html', {'is_contactus_page': True})
