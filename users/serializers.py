from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["id", "date_joined", "updated_at"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class SuperUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["id", "date_joined", "updated_at"]

    def create(self, validated_data):
        return User.create_superuser(**validated_data)


class LoginUserSerializers(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)


class UpdateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["id", 'date_joined', "updated_at"]
        extra_kwargs = {"password": {"write_only": True}}
