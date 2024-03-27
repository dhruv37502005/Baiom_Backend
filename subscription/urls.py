from django.urls import path
from . import views

app_name = 'subscription'

urlpatterns = [
    path('create_purchase_record/', views.create_purchase_record, name='create_purchase_record'),
    path('create-purchase-record/<int:course_id>/<int:plan_id>/<str:username>', views.create_purchase_record, name='create_purchase_record'),
    path('purchase_bootcourse_record/', views.purchase_bootcourse_record, name='purchase_bootcourse_record'),
    path('purchase_itiecourse_record/', views.purchase_itiecourse_record, name='purchase_itiecourse_record'),
    
    # for Json
    path('get-subscription-plans/<int:course_id>/json', views.get_subscription_plans_by_course_id_json, name='get_subscription_plans_by_course_id_json'),
    path('create-purchase-record/<int:course_id>/<int:plan_id>/<str:username>/json', views.create_purchase_record_json, name='create_purchase_record'),
    
]
