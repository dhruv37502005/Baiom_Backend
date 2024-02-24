from django.urls import path
from . import views

app_name = 'subscription'

urlpatterns = [
    path('get-subscription-plans/<int:course_id>/', views.get_subscription_plans_by_course_id, name='get_subscription_plans_by_course_id'),
    path('create-purchase-record/<int:course_id>/<int:plan_id>/', views.create_purchase_record, name='create_purchase_record'),
    ]
