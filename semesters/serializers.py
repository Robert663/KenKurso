from rest_framework import serializers
from .models import Semester


class SemesterSerializers(serializers.ModelSerializer):

    class Meta:
        model = Semester
        fields = "__all__"
        read_only_fields = ["id"]
