from rest_framework import serializers
from students.serializers import StudentSerializer
from .models import School_Record


class SchoolRecordSerializers(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    class Meta:
        model = School_Record
        fields = "__all__"