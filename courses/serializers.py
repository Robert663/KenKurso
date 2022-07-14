from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from courses.models import Course


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_field = ['id', 'created_at']

    def create(self, validated_data):
        return Course.objects.create_user(**validated_data)

class UpdateCourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
