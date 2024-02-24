from datetime import timedelta, timezone
from django.shortcuts import redirect, render

from course.models import Batch, Course
from subscription.models import PurchaseCourse, SubscriptionPlan, SubscriptionPlanCourse

def get_subscription_plans_by_course_id(request, course_id):
    subscription_course_plans = SubscriptionPlanCourse.objects.filter(course_id=course_id)
    print(f"subscription_course_plans: {subscription_course_plans}")
    return render(request, 'subscription_plans_by_course.html', {'subscription_course_plans': subscription_course_plans})

from django.utils import timezone

def create_purchase_record(request, course_id, plan_id):
    # Assuming you have the course_id and plan_id from the URL parameters
    # Retrieve the Dashboard_User associated with the current user
    dashboard_user = request.user.dashboard_user

    # Retrieve the Course, SubscriptionPlan, and Batch objects based on the IDs
    course = Course.objects.get(id=course_id)
    subscription_plan = SubscriptionPlan.objects.get(id=plan_id)
    batch = Batch.objects.get(course=course)

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

    # Redirect to a success page or another URL after enrollment
    return redirect("dashboard:user_ui")
