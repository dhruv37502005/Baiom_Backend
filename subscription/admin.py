from django.contrib import admin

from subscription.models import SubscriptionPlan, SubscriptionPlanCourse, PurchaseCourse

# Register your models here.

class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('name','months')
admin.site.register(SubscriptionPlan,SubscriptionPlanAdmin)

class SubscriptionPlanCourseAdmin(admin.ModelAdmin):
    list_display = ('subscription_plan_name', 'course_name', 'active')

    def subscription_plan_name(self, obj):
        return obj.subscription_plan.name

    def course_name(self, obj):
        return obj.course.title
admin.site.register(SubscriptionPlanCourse,SubscriptionPlanCourseAdmin)

class PurchaseCourseAdmin(admin.ModelAdmin):
    list_display = ('purchased_course', 'subscription_plan', 'dashboard_user', 'purchase_date', 'plans_duration_months')

admin.site.register(PurchaseCourse, PurchaseCourseAdmin)
# admin.site.register(PurchaseCourse)