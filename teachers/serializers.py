from rest_framework import serializers
from .models import Teacher


class TeacherSerializers(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Class.objects.create_user(**validated_data)


class UpdateTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ["id"]
