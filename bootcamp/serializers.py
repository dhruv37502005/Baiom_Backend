from rest_framework import serializers
from bootcamp.models import BootCourse, testimonial

class BootCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BootCourse
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = testimonial
        fields = '__all__'