from django.contrib import admin

from subscription.models import *

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

admin.site.register(PurchaseCourse ,PurchaseCourseAdmin)
# admin.site.register(PurchaseCourse)

class PurchaseBootCampAdmin(admin.ModelAdmin):
    list_display = ('purchased_course', 'subscription_plan', 'dashboard_user', 'purchase_date', 'plans_duration_months')

admin.site.register(PurchaseBootcamp, PurchaseBootCampAdmin)


class SubscriptionPlanItieAdmin(admin.ModelAdmin):
    list_display = ('subscription_plan_name', 'itie_course_name', 'active')

    def subscription_plan_name(self, obj):
        return obj.subscription_plan.name

    def itie_course_name(self, obj):
        return obj.itie_course.title
admin.site.register(SubscriptionPlanItie,SubscriptionPlanItieAdmin)

class SubscriptionPlanBootcampAdmin(admin.ModelAdmin):
    list_display = ('subscription_plan_name', 'bootcamp_course_name', 'active')

    def subscription_plan_name(self, obj):
        return obj.subscription_plan.name

    def bootcamp_course_name(self, obj):
        return obj.bootcamp_course.title
admin.site.register(SubscriptionPlanBootcamp,SubscriptionPlanBootcampAdmin)