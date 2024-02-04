from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from course.models import Course,Purchase, Batch, Resource
from .forms import UserUpdateForm
from userauths.models import Dashboard_User
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.utils import timezone
from datetime import datetime, timedelta

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
                enrolled_courses = dash_user.enrolled_courses.filter(status="active")
                # get batch of that course
                batches = Batch.objects.filter(course__in=enrolled_courses)
                # get notes for that batch
                batch_notes ={}
                for batch in batches:
                    notes = Resource.objects.filter(batch=batch, notes__isnull=False)
                    batch_notes[batch] = notes
                print(f"batch_notes: {batch_notes}")
                print(f"Batch: {batch}")
                print(f"Notes for Batch: {notes}")
                return render(
                    request,
                    "dashboard.html",
                    {
                        "user": user,
                        "dash_user": dash_user,
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
        mobile_number = request.POST.get("mobile_number")
        college_name = request.POST.get("college_name")
        graduation_year = request.POST.get("graduation_year")
        bio = request.POST.get("mobile_number")
        # Update user details
        user_profile.fname = first_name
        user_profile.mname = middle_name
        user_profile.lname = last_name
        user_profile.mobilenumber = mobile_number
        user_profile.collegename = college_name
        user_profile.graduation_year = graduation_year
        user_profile.bio = bio
        # Save changes
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
    dashboard_user, created = Dashboard_User.objects.get_or_create(user=request.user)
    dashboard_user.enrolled_courses.add(course) 
    # messages.success(request, f"You have successfully enrolled in {course.title}.")
    return redirect("dashboard:user_ui")

@login_required(login_url="/userauths/login/")
def enroll_plan(request, date, course_id):
    dashboard_user, created = Dashboard_User.objects.get_or_create(user=request.user)
    course = get_object_or_404(Course, pk=course_id)
    batch = get_object_or_404(Batch, course=course)
    
    start_date = timezone.now()
    end_date = datetime.strptime(date, "%Y-%m-%d")
    additional_access_date = (end_date + timedelta(days=30)).strftime("%Y-%m-%d")
    purchase = Purchase.objects.create(
        user=request.user,
        Batch=batch,
        course=course,
        purchase_start_date=start_date,
        purchase_end_date=end_date,
        additional_access_date=additional_access_date
    )
    dashboard_user.enrolled_courses.add(course)

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