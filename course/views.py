from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from userauths.models import Dashboard_User
from subscription.models import SubscriptionPlanCourse
from userauths.models import Dashboard_User
from .models import Course, CourseCategory, Batch #, Purchase
from wsgiref.util import FileWrapper
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from userauths.models import Dashboard_User
from django.views import View
from .models import CourseCategory, Contact
from django.utils import timezone
from .models import Testimonial
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import Course, CourseCategory, Batch
from .serializers import CourseSerializer, CourseCategorySerializer, BatchSerializer, CourseCarriculumSerializer
from django.views.decorators.csrf import csrf_exempt



# @login_required(login_url='/userauths/login/')
def category_courses(request, category_id):
    category = get_object_or_404(CourseCategory, id=category_id)
    request.session['category_ID'] = category.id
    courses = Course.objects.filter(category=category, status='active')
    categories = CourseCategory.objects.all()
    course = Course.objects.get(id=category_id)
    batches = Batch.objects.get(course=course)
    testimonials = Testimonial.objects.all()
    carriculum = course.curriculum.all()
    subscription_course_plans = SubscriptionPlanCourse.objects.filter(course=course)
    program_overview = course.program_overview.split('\n') if course.program_overview else []

    print(f"subscription_course_plans: {subscription_course_plans}")
    
    user = request.user
    if user.is_authenticated:
        dash_user, created = Dashboard_User.objects.get_or_create(user=user)
        enrolled_courses = dash_user.enrolled_courses.all()
      
        
        return render(request, 'course.html', {
            'is_category': True,
            'courses': courses,
            'carriculum':carriculum,
            'enrolled_courses': enrolled_courses,
            'categories': categories,
            'batch':batches,
            'subscription_course_plans':subscription_course_plans,
            'testimonials': testimonials,
            'program_overview':program_overview,
        })
    else:
        return render(request, 'course.html', {'is_course': True, 'courses': courses,'categories': categories})

@api_view(['GET'])
@csrf_exempt
def category_courses_json(request, category_id):
    category = get_object_or_404(CourseCategory, id=category_id)
    courses = Course.objects.filter(category=category, status='active')
    categories = CourseCategory.objects.all()
    course = Course.objects.get(id=category_id)
    batches = Batch.objects.get(course=course)
    carriculum = course.curriculum.all()
    subscription_course_plans = SubscriptionPlanCourse.objects.filter(course=course)
    
    course_serializer = CourseSerializer(courses, many=True)
    categories_serializer = CourseCategorySerializer(categories, many=True)
    batch_serializer = BatchSerializer(batches)
    course_carriculum_serializer = CourseCarriculumSerializer(carriculum, many=True)
    jsondata = {
            'courses': course_serializer.data,
            'batch': batch_serializer.data,
            'categories': categories_serializer.data,
            'carriculum': course_carriculum_serializer.data,
        }
    return Response(jsondata)



# @api_view(['GET'])
# def category_courses(request, category_id):
#     # Retrieve data from database
#     category = get_object_or_404(CourseCategory, id=category_id)
#     courses = Course.objects.filter(category=category, status='active')
#     categories = CourseCategory.objects.all()
#     course = Course.objects.get(id=category_id)
#     batches = Batch.objects.get(course=course)
#     carriculum = course.curriculum.all()
#     subscription_course_plans = SubscriptionPlanCourse.objects.filter(course=course)
#     print(f"subscription_course_plans: {subscription_course_plans}")
#     enrolled_courses = dash_user.enrolled_courses.all()
    
#     # Prepare data for response
#     user = request.user
#     if user.is_authenticated:
#         dash_user, created = Dashboard_User.objects.get_or_create(user=user)
#         enrolled_courses = dash_user.enrolled_courses.all()
        
#         course_serializer = CourseSerializer(courses, many=True)
#         categories_serializer = CourseCategorySerializer(categories, many=True)
#         batch_serializer = BatchSerializer(batches)
#         course_carriculum_serializer = CourseCarriculumSerializer(carriculum, many=True)

#         data = {
#             'is_category': True,
#             'courses': course_serializer.data,
#             'categories': categories_serializer.data,
#             'batch': batch_serializer.data,
#             'carriculum': course_carriculum_serializer.data,
#         }
#         course_serializer = CourseSerializer(courses, many=True)
#         batch_serializer = BatchSerializer(batches)
#         categories_serializer = CourseCategorySerializer(categories, many=True)
#         course_carriculum_serializer = CourseCarriculumSerializer(carriculum, many=True)

#         jsondata = {
#             'courses': course_serializer.data,
#             'batch': batch_serializer.data,
#             'categories': categories_serializer.data,
#             'carriculum': course_carriculum_serializer.data,
#         }
    
#     # Check if the request wants JSON response
#     if request.accepted_renderer.format == 'json':
#         return JsonResponse(jsondata)
#     else:
#         # Render HTML template
#         # template_data = data.copy()  # Copy the data to avoid modification of the original dictionary
#         return render(request, 'course.html', {
#             'is_category': True,
#             'courses': courses,
#             'carriculum':carriculum,
#             'enrolled_courses': enrolled_courses,
#             'categories': categories,
#             'batch':batches,
#             'subscription_course_plans':subscription_course_plans
#         })

# @api_view(['GET'])
# def category_courses_json(request, category_id):
#     # Retrieve data from database
#     category = get_object_or_404(CourseCategory, id=category_id)
#     courses = Course.objects.filter(category=category, status='active')
    
#     # Serialize data
#     course_serializer = CourseSerializer(courses, many=True)
#     course_category_serializer = CourseCategorySerializer(CourseCategory, many=True)
#     batch_serializer = BatchSerializer(Batch, many=True)
#     data = {
#         'courses': course_serializer.data,
#         'category': course_category_serializer.data,
#         'batch':batch_serializer.data,
#     }
    
#     return Response(data)



class DownloadFileView(View):
    def get(self, category_id,file_id):
        category_id = file_id
        category = get_object_or_404(CourseCategory, pk=file_id)
        file_content = category.file.read()
        file_name = category.file.name
        response = HttpResponse(file_content, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'

        return response

# login_required(login_url='/userauths/login/')
def course_contact(request):
    if request.method == 'POST':
        name_ = request.POST.get('name_')
        email_ = request.POST.get('email_')
        mobile_ = request.POST.get('mobile_')
        profession_ = request.POST.get('profession_')
        contact_obj = Contact(name=name_,email=email_,mobile=mobile_,profession=profession_)
        contact_obj.save()
        messages.success(request,'thank you for contacting us')
        return redirect('course:category_courses', category_id=request.session['category_ID'])