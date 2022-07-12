from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model: User
        fields = "__all__"
        read_only_fields = ["id", "date_joined"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginUserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UpdateUserSerializers(serializers.ModelSerializer):

    class Meta:
        model: User
        fields: "__all__"
        read_only_fields = ["id", 'date_joined']
        extra_kwargs = {"password": {"write_only": True}}
