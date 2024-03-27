from datetime import timedelta, timezone
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .serializers import *
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from course.models import Batch, Course
from subscription.models import *
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from userauths.models import  Dashboard_User
from subscription.models import *
from bootcamp.models import BootCourse, BootBatch
from itie.models import IBatch, ICourse

def get_subscription_plans_by_course_id(request, course_id):
    subscription_course_plans = SubscriptionPlanCourse.objects.filter(course_id=course_id)
    return render(request, 'subscription_plans_by_course.html', {'subscription_course_plans': subscription_course_plans})

def get_subscription_plans_by_course_id_json(request, course_id):
    subscription_course_plans = SubscriptionPlanCourse.objects.filter(course_id=course_id)
    subscription_course_plans_serialized = SubscriptionPlanCourseSerializer(subscription_course_plans, many=True)
    return JsonResponse({"SubscriptionCoursePlans":subscription_course_plans_serialized.data})
    
@login_required(login_url='/userauths/login/')
def create_purchase_record(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        plan_id = request.POST.get('plan_id')
        username = request.POST.get('username')
        
        user = User.objects.get(username=username)
        dashboard_user = Dashboard_User.objects.get(user=user)
        course = Course.objects.get(id=course_id)
        subscription_plan = SubscriptionPlan.objects.get(id=plan_id)
        batch = Batch.objects.get(course=course)
        if course in dashboard_user.enrolled_courses.all():
            messages.error(request, "Course is already enrolled.")
            return redirect("core:index")
        purchase_date = timezone.now().date()
        purchase_start_date = purchase_date
        plans_duration_months = subscription_plan.months
        purchase_end_date = purchase_start_date + timedelta(days=30 * plans_duration_months)
        additional_access_date = purchase_end_date  # Additional access date if needed

        # Create PurchaseCourse record
        purchase_course = PurchaseCourse.objects.create(
            dashboard_user=dashboard_user,
            purchased_course=course,
            subscription_plan=subscription_plan,
            Batch=batch,
            purchase_date=purchase_date,
            plans_duration_months=plans_duration_months,
            purchase_start_date=purchase_start_date,
            purchase_end_date=purchase_end_date,
            additional_access_date=additional_access_date
        )
        dashboard_user.enrolled_courses.add(course)
        dashboard_user.enrolled_batches.add(batch)

        messages.success(request, "Course successfully purchased. Check your dashboard.")
        return redirect("core:index")

    else:
        # Handle if the request method is not POST
        return redirect("core:index")  # Redirect to some appropriate page if needed





def create_purchase_record_json(request, course_id, plan_id, username):
    # Assuming you have the course_id and plan_id from the URL parameters
    # Retrieve the Dashboard_User associated with the current user
    user = User.objects.get(username= username)
    dashboard_user = Dashboard_User.objects.get(user=user)

    # Retrieve the Course, SubscriptionPlan, and Batch objects based on the IDs
    course = Course.objects.get(id=course_id)
    subscription_plan = SubscriptionPlan.objects.get(id=plan_id)
    batch = Batch.objects.get(course=course)
    
    purchase_course = PurchaseCourse.objects.filter(dashboard_user=dashboard_user, purchased_course=course, subscription_plan=subscription_plan, Batch=batch)
 
    if purchase_course.exists():
        return JsonResponse({"result": "Course is already enrolled."})

    # Calculate purchase dates and duration based on the subscription plan
    purchase_date = timezone.now().date()
    purchase_start_date = purchase_date
    purchase_end_date = purchase_start_date + timedelta(days=30 * subscription_plan.months)
    additional_access_date = purchase_end_date  # Additional access date if needed

    # Create and save the PurchaseCourse record
    purchase_course = PurchaseCourse.objects.create(
        dashboard_user=dashboard_user,
        purchased_course=course,
        subscription_plan=subscription_plan,
        Batch=batch,
        purchase_date=purchase_date,
        plans_duration_months=subscription_plan.months,
        purchase_start_date=purchase_start_date,
        purchase_end_date=purchase_end_date,
        additional_access_date=additional_access_date
    )
    purchase_course_serializer = PurchaseCourseSerializer(purchase_course)

    return JsonResponse({"PurchaseCourses":purchase_course_serializer.data})


@login_required(login_url='/userauths/login/')
def purchase_bootcourse_record(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        plan_id = request.POST.get('plan_id')
        print(plan_id)
        username = request.POST.get('username')
        
        user = User.objects.get(username=username)
        dashboard_user = Dashboard_User.objects.get(user=user)
        course = BootCourse.objects.get(id=course_id)
        subscription_plan = SubscriptionPlan.objects.get(id=plan_id)
        batch = BootBatch.objects.get(course=course)
        if course in dashboard_user.enrolled_bootcourses.all():
            messages.error(request, "Course is already enrolled.")
            return redirect("core:index")
        purchase_date = timezone.now().date()
        purchase_start_date = purchase_date
        plans_duration_months = subscription_plan.months
        purchase_end_date = purchase_start_date + timedelta(days=30 * plans_duration_months)
        additional_access_date = purchase_end_date  # Additional access date if needed

        # Create PurchaseCourse record
        purchase_course = PurchaseBootcamp.objects.create(
            dashboard_user=dashboard_user,
            purchased_course=course,
            subscription_plan=subscription_plan,
            Batch=batch,
            purchase_date=purchase_date,
            plans_duration_months=plans_duration_months,
            purchase_start_date=purchase_start_date,
            purchase_end_date=purchase_end_date,
            additional_access_date=additional_access_date
        )
        dashboard_user.enrolled_bootcourses.add(course)
        dashboard_user.enrolled_bootbatches.add(batch)

        messages.success(request, "Bootcamp Course successfully purchased. Check your dashboard.")
        return redirect("core:index")

    else:
        # Handle if the request method is not POST
        return redirect("core:index")  # Redirect to some appropriate page if needed


@login_required(login_url='/userauths/login/')
def purchase_itiecourse_record(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        plan_id = request.POST.get('plan_id')
        print(plan_id)
        username = request.POST.get('username')
        
        user = User.objects.get(username=username)
        dashboard_user = Dashboard_User.objects.get(user=user)
        course = ICourse.objects.get(id=course_id)
        subscription_plan = SubscriptionPlan.objects.get(id=plan_id)
        batch = IBatch.objects.get(course=course)
        if course in dashboard_user.enrolled_itiecourses.all():
            messages.error(request, "Course is already enrolled.")
            return redirect("core:index")
        purchase_date = timezone.now().date()
        purchase_start_date = purchase_date
        plans_duration_months = subscription_plan.months
        purchase_end_date = purchase_start_date + timedelta(days=30 * plans_duration_months)
        additional_access_date = purchase_end_date  # Additional access date if needed

        # Create PurchaseCourse record
        purchase_course = PurchaseItie.objects.create(
            dashboard_user=dashboard_user,
            purchased_course=course,
            subscription_plan=subscription_plan,
            Batch=batch,
            purchase_date=purchase_date,
            plans_duration_months=plans_duration_months,
            purchase_start_date=purchase_start_date,
            purchase_end_date=purchase_end_date,
            additional_access_date=additional_access_date
        )
        dashboard_user.enrolled_itiecourses.add(course)
        dashboard_user.enrolled_itiebatches.add(batch)

        messages.success(request, "ITIE Course successfully purchased. Check your dashboard.")
        return redirect("core:index")

    else:
        # Handle if the request method is not POST
        return redirect("core:index")  # Redirect to some appropriate page if needed
