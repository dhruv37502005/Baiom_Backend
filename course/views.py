from django.shortcuts import render, redirect


from .models import Course

# Create your views here.
def webdevelopment(request):
    # courses = Course.objects.all()
    web_dev_courses = Course.objects.filter(category='Web Development', status='active')
    print(web_dev_courses)
    return render(request, 'webdevelopment.html', {'is_webdevelopment_page': True, 'web_dev_courses': web_dev_courses})

# def datascience(request):
#     data_science_courses = Course.objects.filter(category='Data Science', status='active')
#     return render(request, 'webdevelopment.html', {'is_webdevelopment_page': True, 'web_dev_courses': web_dev_courses})


def dashboard_view(request):
    all_courses = Course.objects.all()
    return render(request, 'dashboard.html',{'is_dashboard_page': True, 'all_courses': all_courses})


# def courses(request):
#     course = Course.objects.all()
#     context={
#         'course': course,
#     }
#     print(course)
#     return render(request, 'webdevelopment.html', context)