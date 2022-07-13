from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Class


class ClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        return Class.objects.create_user(**validated_data)


class UpdateClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
