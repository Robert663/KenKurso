from rest_framework import serializers
from .models import Teacher


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
        read_only_field = ['updated_at']

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)


class UpdateTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'
