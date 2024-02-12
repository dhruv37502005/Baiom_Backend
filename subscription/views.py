from django.shortcuts import render

from course.models import Course
from subscription.models import SubscriptionPlan, SubscriptionPlanCourse

def get_subscription_plans_by_course_id(request, course_id):
    subscription_course_plans = SubscriptionPlanCourse.objects.filter(course_id=course_id)
    print(f"subscription_course_plans: {subscription_course_plans}")
    return render(request, 'subscription_plans_by_course.html', {'subscription_course_plans': subscription_course_plans})