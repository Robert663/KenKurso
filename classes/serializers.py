from rest_framework.serializers import ModelSerializer
from .models import Class


class ClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
        read_only_fields = ['id', 'created_at','subject']

    def create(self, validated_data):
        return Class.objects.create(**validated_data)


class UpdateClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
