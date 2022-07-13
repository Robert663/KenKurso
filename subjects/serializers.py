from rest_framework import serializers
from .models import Subject


class SubjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
