from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from course.models import Course, Batch, Resource #,Purchase
from .forms import UserUpdateForm
from userauths.models import Dashboard_User
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile


@login_required(login_url="/userauths/login/")
@transaction.atomic
# FIXME: this function is handling multiple API's calls need to make sub-fuctions to pass context
# TODO: seperate POST and GET API from this function
def user_ui(request):
    if request.method == "GET":
        auser = request.user
        if request.user.is_authenticated:
            if auser.is_staff == True:
                return redirect("/admin")
            else:
                # username = request.session['username']
                user = User.objects.get(username=request.user.username)
                if not Dashboard_User.objects.filter(user_id=user.id).exists():
                    dashboard_user, created = Dashboard_User.objects.get_or_create(user=auser)
                    dashboard_user.save()
                dash_user = Dashboard_User.objects.get(user_id=user.id)
                # get active courses if enrolled
                # enrolled_courses = dash_user.enrolled_courses.filter(status="active")
                purchase_courses = Purchase.objects.filter(user=request.user)
                todays_date = timezone.now().date()
                print(todays_date)

                enrolled_courses = dash_user.enrolled_courses.filter(status="active")
                # purchase_courses = Purchase.objects.filter(user=request.user)
                todays_date = timezone.now().date()
                print(todays_date)
                # TODO:  pass final purchase query to dashboard
                # ongoing_courses = [purchase.course  for purchase in purchase_courses
                #     if (purchase.purchase_end_date and purchase.additional_access_date) >todays_date]
                # print(f"ongoing_courses: {ongoing_courses}")
                years = list(range(1990, 2031))


                # get active courses if enrolled
                enrolled_courses = dash_user.enrolled_courses.filter(status="active")
                # purchase_courses = Purchase.objects.filter(user=request.user)
                todays_date = timezone.now().date()
                print(todays_date)
                # TODO:  pass final purchase query to dashboard
                # ongoing_courses = [purchase.course  for purchase in purchase_courses
                #     if (purchase.purchase_end_date and purchase.additional_access_date) >todays_date]
                # print(f"ongoing_courses: {ongoing_courses}")
                years = list(range(1990, 2031))

                # get batch of that course
                batches = Batch.objects.filter(course__in=enrolled_courses)
                print(f"batches: {batches}")
                # get batch of that course
                batches = Batch.objects.filter(course__in=enrolled_courses)
                # get notes for that batch
                batch_notes ={}
                for batch in batches:
                    notes = Resource.objects.filter(batch=batch, notes__isnull=False)
                    batch_notes[batch] = notes


                return render(
                    request,
                    "dashboard.html",
                    {
                        'years': years,
                        "user": user,
                        "dash_user": dash_user,
                        # "enrolled_courses": ongoing_courses,
                        "enrolled_courses": enrolled_courses,
                        "batches": batches,
                        "batch_notes": batch_notes,
                    },
                )
        # FIXME handling POST request  
        else:
            # TODO: NEED TO CREATE A NE POST API FOR USER UPDATE
            return redirect("userauths:login")
    if request.method == "POST":
        user_profile = Dashboard_User.objects.get(user=request.user)

        
    if request.method == "POST":
      #get from frontend
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        college_name = request.POST.get("college_name")
        graduation_year = request.POST.get("graduation_year")
        mobile_number = request.POST.get("mobile_number")
        bio = request.POST.get("bio")
        education =request.POST.get("education")
        github = request.POST.get("github")
        linkedin = request.POST.get("linkedin")

        if not education:
            education = "No Education Provided"

      

        print(first_name, middle_name, last_name, college_name, education, graduation_year, mobile_number, github, linkedin, bio)
        # Update user details
        user_profile.fname = first_name
        user_profile.mname = middle_name
        user_profile.lname = last_name
        user_profile.mobilenumber = mobile_number
        user_profile.collegename = college_name
        user_profile.graduation_year = graduation_year
        user_profile.education = education
        user_profile.github = github
        user_profile.linkedin = linkedin
        user_profile.bio = bio
        # Save changes
        profile_photo = request.FILES.get('profile_photo')
        print("profile is :", profile_photo)
        if profile_photo:
            fs = FileSystemStorage()
            file_path = fs.save(f'user_photos/{request.user.username}/{profile_photo.name}', ContentFile(profile_photo.read()))
            print("File saved to:", file_path)
            user_profile.photo = file_path

       
        # user_profile.save()
        user_profile.save()
        # messages.success(request, "Profile updated successfully")
        return redirect("dashboard:user_ui")
    return render(request, "dashboard.html", {"user": request.user})


def admin_ui(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            auser = request.user
            if auser.is_staff == True:
                return redirect("core:index")
            else:
                return redirect("/admin")
        else:
            return redirect("core:index")



@login_required(login_url="/userauths/login/")
def enroll_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    batches = Batch.objects.filter(course_id=course_id)

    if request.method == "POST":
        batch_id = request.POST.get("batch_id")
        if batch_id:
            batch = get_object_or_404(Batch, pk=batch_id)
            dashboard_user, created = Dashboard_User.objects.get_or_create(user=request.user)
            dashboard_user.enrolled_batches.add(batch)
    return redirect("dashboard:user_ui")  # Redirect to the dashboard



@login_required(login_url="/userauths/login/")
def enroll_plan(request, date, course_id):
    dashboard_user, created = Dashboard_User.objects.get_or_create(user=request.user)
    course = get_object_or_404(Course, pk=course_id)
    batch = get_object_or_404(Batch, course_id=course_id)
    
    start_date = timezone.now()
    end_date = datetime.strptime(date, "%Y-%m-%d")
    additional_access_date = (end_date + timedelta(days=30)).strftime("%Y-%m-%d")
    # purchase = Purchase.objects.create(
    #     user=request.user,
    #     Batch=batch,
    #     course=course,
    #     purchase_start_date=start_date,
    #     purchase_end_date=end_date,
    #     additional_access_date=additional_access_date
    # )
    dashboard_user.enrolled_courses.add(course)
    dashboard_user.enrolled_batches.add(batch)

    return redirect("dashboard:user_ui")




# @login_required(login_url="/userauths/login/")
# def enroll_course(request, course_id):
    # course = get_object_or_404(Course, pk=course_id)
    # dashboard_user, created = Dashboard_User.objects.get_or_create(user=request.user)
    #save course on dash_user
    # dashboard_user.enrolled_courses.add(course)
    # messages.success(request, f"You have successfully enrolled in {course.title}.")

    #find batch of that course 
    #save batch
    #get curr_date
    #calculate end date
    #calculate additional date
    #save that purchase with course, batch, dash_user details
    #end

    # batches = Batch.objects.all()
    # if request.method == 'POST':
    #     batch_id = request.POST.get('batch_id')
    #     batch = Batch.objects.get(id=batch_id)
        # Customizing start and end dates based on user's package choice
        # package_duration = int(request.POST.get('package_duration'))  # Assuming a form field for package duration
        #date calculation
        # start_date = timezone.now().date()
        # end_date = start_date + timedelta(days=package_duration * 30)  # Assuming each month has 30 days
        
        #save these dates on purchse start and end with dash_user, course_id, batch_id
        # batch.start_date = start_date
        # batch.end_date = end_date
        # batch.save()
        # dashboard_user.enrolled_batches.add(batch)
    
    # return redirect("dashboard:user_ui")