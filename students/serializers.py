

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        return Student.objects.create_user(**validated_data)


class UpdateStudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class DeactiveStudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['active']

    def update(self, instance, validated_data):
        validated_data['active'] = False
        return super().update(instance, validated_data)
