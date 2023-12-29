from django.shortcuts import render
from django.shortcuts import render
from .models import contact

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number') 
        message = request.POST.get('msg')

        contact_obj = contact(name=name, email=email, phone=phone, content=message)
        contact_obj.save()

        return render(request, 'contact-us.html', {'thank_you_message': 'Thank you for contacting us!'})

    return render(request, 'contact-us.html', {'is_contactus_page': True})
