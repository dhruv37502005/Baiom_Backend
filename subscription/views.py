from datetime import timedelta, timezone
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from course.models import Batch, Course
from subscription.models import PurchaseCourse, SubscriptionPlan, SubscriptionPlanCourse
from userauths.models import Dashboard_User

def get_subscription_plans_by_course_id(request, course_id):
    subscription_course_plans = SubscriptionPlanCourse.objects.filter(course_id=course_id)
    print(f"subscription_course_plans: {subscription_course_plans}")
    return render(request, 'subscription_plans_by_course.html', {'subscription_course_plans': subscription_course_plans})

from django.utils import timezone

@login_required(login_url='/userauths/login/')
def create_purchase_record(request, course_id, plan_id):
    dashboard_user, created = Dashboard_User.objects.get_or_create(user=request.user)
    course = Course.objects.get(id=course_id)
    subscription_plan = SubscriptionPlan.objects.get(id=plan_id)
    batch = Batch.objects.get(course=course)
    purchase_date = timezone.now().date()
    purchase_start_date = purchase_date
    purchase_end_date = purchase_start_date + timedelta(days=30 * subscription_plan.months)
    additional_access_date = purchase_end_date  # Additional access date if needed
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
    dashboard_user.enrolled_courses.add(course)
    dashboard_user.enrolled_batches.add(batch) # Add the batch to enrolled_batches
    dashboard_user.save()
    return redirect("dashboard:user_ui")
