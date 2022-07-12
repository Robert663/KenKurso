from rest_framework import serializers
from .models import Teacher


class TeacherSerializers(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"

    def create(self, validated_data):

        return Teacher.objects.create_user(**validated_data)


class UpdateTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'
