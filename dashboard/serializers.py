from rest_framework import serializers
from course.models import *
from django.contrib.auth.models import User
from userauths.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
        

class Dash_userSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    enrolled_courses = CourseSerializer(read_only=True, many=True)
    enrolled_batches = BatchSerializer(read_only=True, many=True)
    curriculum = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    
    class Meta:
        model = Dashboard_User
        fields = '__all__'
    
    def get_curriculum(self, obj):
        # Retrieve curriculum for each enrolled course
        return [curriculum.carriculum_title for course in obj.enrolled_courses.all() for curriculum in course.curriculum.all()]

    def get_category(self, obj):
        # Retrieve category for each enrolled course
        return [course.category.name for course in obj.enrolled_courses.all()]


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




# class CourseCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CourseCategory
#         fields = '__all__'


# class CourseCarriculumSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CourseCarriculum
#         fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'