from rest_framework import serializers
from .models import *


class SubscriptionPlanCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlanCourse
        fields = '__all__'

class PurchaseCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseCourse
        fields = '__all__'