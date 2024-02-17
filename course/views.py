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
from .models import CourseCategory

from django.utils import timezone

# @login_required(login_url='/userauths/login/')
# def category_courses(request, category_id):
#     category = get_object_or_404(CourseCategory, id=category_id)
#     courses = Course.objects.filter(category=category, status='active')
#     categories = CourseCategory.objects.all()
#     course = Course.objects.get(id=category_id)
#     batches = Batch.objects.get(course=course)
#     carriculum = course.curriculum.all()
#     subscription_course_plans = SubscriptionPlanCourse.objects.filter(course=course)
#     print(f"subscription_course_plans: {subscription_course_plans}")
    
#     user = request.user
#     if user.is_authenticated:
#         dash_user, created = Dashboard_User.objects.get_or_create(user=user)
#         enrolled_courses = dash_user.enrolled_courses.all()
      
        
#         return render(request, 'course.html', {
#             'is_category': True,
#             'courses': courses,
#             'carriculum':carriculum,
#             'enrolled_courses': enrolled_courses,
#             'categories': categories,
#             'batch':batches,
#             'subscription_course_plans':subscription_course_plans
#         })
#     else:
#         return render(request, 'course.html', {'is_course': True, 'courses': courses})




from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import Course, CourseCategory, Batch
from .serializers import CourseSerializer, CourseCategorySerializer, BatchSerializer, CourseCarriculumSerializer

from rest_framework.response import Response

@api_view(['GET'])
def category_courses(request, category_id):
    # Retrieve data from database
    category = get_object_or_404(CourseCategory, id=category_id)
    courses = Course.objects.filter(category=category, status='active')
    categories = CourseCategory.objects.all()
    course = Course.objects.get(id=category_id)
    batches = Batch.objects.get(course=course)
    carriculum = course.curriculum.all()
    subscription_course_plans = SubscriptionPlanCourse.objects.filter(course=course)
    print(f"subscription_course_plans: {subscription_course_plans}")
    
    # Prepare data for response
    user = request.user
    if user.is_authenticated:
        dash_user, created = Dashboard_User.objects.get_or_create(user=user)
        enrolled_courses = dash_user.enrolled_courses.all()
        
        course_serializer = CourseSerializer(courses, many=True)
        categories_serializer = CourseCategorySerializer(categories, many=True)
        batch_serializer = BatchSerializer(batches)
        course_carriculum_serializer = CourseCarriculumSerializer(carriculum, many=True)

        data = {
            'is_category': True,
            'courses': course_serializer.data,
            'categories': categories_serializer.data,
            'batch': batch_serializer.data,
            'carriculum': course_carriculum_serializer.data,
        }
    else:
        course_serializer = CourseSerializer(courses, many=True)
        batch_serializer = BatchSerializer(batches)
        categories_serializer = CourseCategorySerializer(categories, many=True)
        course_carriculum_serializer = CourseCarriculumSerializer(carriculum, many=True)

        jsondata = {
            'courses': course_serializer.data,
            'batch': batch_serializer.data,
            'categories': categories_serializer.data,
            'carriculum': course_carriculum_serializer.data,
        }
    
    # Check if the request wants JSON response
    if request.accepted_renderer.format == 'json':
        return JsonResponse(jsondata)
    else:
        # Render HTML template
        template_data = data.copy()  # Copy the data to avoid modification of the original dictionary
        return render(request, 'course.html', context=template_data)

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
# def categories(request):
#     categories = CourseCategory.objects.all()
#     print(categories)
#     return render(request, 'test.html', {'categories': categories})
# @login_required(login_url='/userauths/login/')

# def webdevelopment(request):
#     web_dev_courses = Course.objects.filter(category='Web Development', status='active')
#     user = request.user
#     if user.is_authenticated:
#         dash_user, created = Dashboard_User.objects.get_or_create(user=user)
#         enrolled_courses = dash_user.enrolled_courses.all()
#         categories = CourseCategory.objects.all()
#         print(categories)
#         return render(request, 'webdevelopment.html', {
#             'is_webdevelopment_page': True,
#             'web_dev_courses': web_dev_courses,
#             'enrolled_courses': enrolled_courses,
#             'categories':categories
#         })
#     else:
#         return render(request, 'webdevelopment.html', {
#             'is_webdevelopment_page': True,
#             'web_dev_courses': web_dev_courses
#         })
# def dataanalyst(request):
#     data_analyst_courses = Course.objects.filter(category='Data Analyst', status='active')
#     return render(request, 'dataanalyst.html', {'is_dataanalyst_page': True, 'data_analyst': data_analyst_courses})

# def datascience(request):
#     data_science_courses = Course.objects.filter(category='Data Science', status='active')
#     return render(request, 'datascience.html', {'is_datascience_page': True, 'data_science_courses': data_science_courses})


# def contentwriting(request):
#     content_Writing_courses = Course.objects.filter(category='content Writing', status='active')
#     return render(request, 'contentwriting.html', {'is_contentWriting_page': True, 'content_Writing': content_Writing_courses})

# def graphicdesigning(request):
#     graphic_designing_courses = Course.objects.filter(category='Graphic Designing', status='active')
#     return render(request, 'graphicdesigning.html', {'is_graphicdesigning_page': True, 'graphic_designing': graphic_designing_courses})

# def seomarketing(request):
#     seo_marketing_courses = Course.objects.filter(category='SEO Marketing', status='active')
#     return render(request, 'seomarketing.html', {'is_seomarketing_page': True, 'seo_marketing': seo_marketing_courses})


# def digitalmarketing(request):
#     digital_marketing_courses = Course.objects.filter(category='Digital Marketing', status='active')
#     return render(request, 'digitalmarketing.html', {'is_digitalmarketing_page': True, 'digital_marketing': digital_marketing_courses})

# def projectmanagement(request):
#     project_management_courses = Course.objects.filter(category='Project Management', status='active')
#     return render(request, 'projectmanagement.html', {'is_projectmanagement_page': True, 'projectmanagement': project_management_courses})

# def humanresource(request):
#     human_resource_courses = Course.objects.filter(category='Human Resource', status='active')
#     return render(request, 'humanresource.html', {'is_humanresource_page': True, 'human_resource': human_resource_courses})

# def corporatelaw(request):
#     corporate_law_courses = Course.objects.filter(category='Corporate  Law', status='active')
#     return render(request, 'corporatelaw.html', {'is_corporatelaw_page': True, 'corporate_law': corporate_law_courses})

# def enterpreneurship(request):
#     enterpreneurship_courses = Course.objects.filter(category='Enterpreneurship', status='active')
#     return render(request, 'enterpreneurship.html', {'is_enterpreneurship_page': True, 'enterpreneurship': enterpreneurship_courses})


##

#def watch_video(request, course_id):
    # Assuming you have a Course model with a video_name field
    # course = Course.objects.get(id=course_id)
    # video_path = "{Course.video_name}"

    # cap = cv2.VideoCapture(video_path)
    # start_time = cv2.getTickCount()

    # while cap.isOpened():
    #     ret, frame = cap.read()

    #     if not ret:
    #         break  # Break the loop if there are no more frames to read

    #     cv2.imshow("Video", frame)

    #     if cv2.waitKey(30) & 0xFF == 27:  # Press 'Esc' to exit
    #         break

    # end_time = cv2.getTickCount()
    # elapsed_time = (end_time - start_time) / cv2.getTickFrequency()

    #  # Save the elapsed_time in the watchedTime field of the DashboardUser model
    # dashboard_user, created = Dashboard_User.objects.get_or_create(user=request.user)
    # dashboard_user.watchedTime += elapsed_time
    # dashboard_user.save()

    # # Here, you can save the elapsed_time in your database or perform other actions
    # # For simplicity, let's just print the time
    # print(f"User watched the video for {elapsed_time:.2f} seconds")

    # cap.release()
    # cv2.destroyAllWindows()

    # return HttpResponse("Video watched successfully!")





#def user_progress(request,course_id):
 #   course = get_object_or_404(Course,pk=course.id)
    #current user logged in
  #  user = request.user
   # videos = course.videos.all()
    #total_duration = sum(video.duration for video in videos)
    #course.duration_field = total_duration
    #Course.save()
    #watched_duration = Course.objects.filter(user=user, video__in=videos).aggregate(models.Sum('watched_duration'))['watched_duration__sum']
    #progress_percentage = (watched_duration / total_duration) * 100 if total_duration > 0 else 0
    #context = {
     #   'course': course,
      #  'progress_percentage': progress_percentage,
    #}

    
    #return render(request,'dashboard.html', context)






