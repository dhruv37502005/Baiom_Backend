from rest_framework import serializers
from course.models import *
from django.contrib.auth.models import User
from userauths.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Dash_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard_User
        fields = '__all__'
        

class ProfileDataSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    last_name = serializers.CharField()
    college_name = serializers.CharField()
    graduation_year = serializers.IntegerField()
    mobile_number = serializers.CharField()
    bio = serializers.CharField()
    education = serializers.CharField()
    github = serializers.CharField()
    linkedin = serializers.CharField()
    # profile = serializers.ImageField()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

# class CourseCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CourseCategory
#         fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
        
# class CourseCarriculumSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CourseCarriculum
#         fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'