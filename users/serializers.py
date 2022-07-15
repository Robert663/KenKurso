from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


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

    def update(self, instance: User, validated_data):
        non_editable_keys = ()
        for key, value in validated_data.items():
            if key in non_editable_keys:
                raise KeyError
            setattr(instance, key, value)
        if "password" in validated_data:
            hashed_password = make_password(validated_data["password"])
            setattr(instance, "password", hashed_password)
        instance.save()
        return instance