from rest_framework import serializers
from bootcamp.models import BootCourse, testimonial, BootBatch

class BootBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BootBatch
        fields = '__all__'

class BootCourseSerializer(serializers.ModelSerializer):
    batches = BootBatchSerializer(many=True, read_only=True)
    class Meta:
        model = BootCourse
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = testimonial
        fields = '__all__'


