from django.shortcuts import render, redirect
from .models import Course

def webdevelopment(request):
    # courses = Course.objects.all()
    web_dev_courses = Course.objects.filter(category='Web Development', status='active')
    print(web_dev_courses)
    return render(request, 'webdevelopment.html', {'is_webdevelopment_page': True, 'web_dev_courses': web_dev_courses})

def dataanalyst(request):
    data_analyst_courses = Course.objects.filter(category='Data Analyst', status='active')
    return render(request, 'dataanalyst.html', {'is_dataanalyst_page': True, 'data_analyst': data_analyst_courses})

def datascience(request):
    data_science_courses = Course.objects.filter(category='Data Science', status='active')
    return render(request, 'datascience.html', {'is_datascience_page': True, 'data_science_courses': data_science_courses})


def contentwriting(request):
    content_Writing_courses = Course.objects.filter(category='content Writing', status='active')
    return render(request, 'contentwriting.html', {'is_contentWriting_page': True, 'content_Writing': content_Writing_courses})

def graphicdesigning(request):
    graphic_designing_courses = Course.objects.filter(category='Graphic Designing', status='active')
    return render(request, 'graphicdesigning.html', {'is_graphicdesigning_page': True, 'graphic_designing': graphic_designing_courses})

def seomarketing(request):
    seo_marketing_courses = Course.objects.filter(category='SEO Marketing', status='active')
    return render(request, 'seomarketing.html', {'is_seomarketing_page': True, 'seo_marketing': seo_marketing_courses})


def digitalmarketing(request):
    digital_marketing_courses = Course.objects.filter(category='Digital Marketing', status='active')
    return render(request, 'digitalmarketing.html', {'is_digitalmarketing_page': True, 'digital_marketing': digital_marketing_courses})

def projectmanagement(request):
    project_management_courses = Course.objects.filter(category='Project Management', status='active')
    return render(request, 'projectmanagement.html', {'is_projectmanagement_page': True, 'projectmanagement': project_management_courses})

def humanresource(request):
    human_resource_courses = Course.objects.filter(category='Human Resource', status='active')
    return render(request, 'humanresource.html', {'is_humanresource_page': True, 'human_resource': human_resource_courses})

def corporatelaw(request):
    corporate_law_courses = Course.objects.filter(category='Corporate  Law', status='active')
    return render(request, 'corporatelaw.html', {'is_corporatelaw_page': True, 'corporate_law': corporate_law_courses})

def enterpreneurship(request):
    enterpreneurship_courses = Course.objects.filter(category='Enterpreneurship', status='active')
    return render(request, 'enterpreneurship.html', {'is_enterpreneurship_page': True, 'enterpreneurship': enterpreneurship_courses})

