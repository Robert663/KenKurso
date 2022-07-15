

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from users.serializers import UserSerializers

from .models import Student

class StudentSerializer(ModelSerializer):
    user = UserSerializers(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        depth=2

    def create(self, validated_data):
        return Student.objects.create(**validated_data)


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
