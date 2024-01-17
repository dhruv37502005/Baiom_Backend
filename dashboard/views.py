from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from course.models import Course
from .forms import UserUpdateForm
from userauths.models import Dashboard_User
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction

@login_required(login_url="/userauths/login/")
@transaction.atomic
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
                # all_courses = Course.objects.all()
                enrolled_courses = dash_user.enrolled_courses.filter(status="active")
                return render(
                    request,
                    "dashboard.html",
                    {
                        "user": user,
                        "dash_user": dash_user,
                        "enrolled_courses": enrolled_courses,
                    },
                )
        else:
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

