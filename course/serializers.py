from rest_framework import serializers
from .models import Course, CourseCategory, Batch,CourseCarriculum

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
        
class CourseCarriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCarriculum
        fields = '__all__'
