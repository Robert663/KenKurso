from rest_framework import serializers
from .models import Semester


class SemesterSerializers(serializers.ModelSerializer):

    class Meta:
        model = Semester
        fields = ["id","semester", "course_id", "subjects_id"]


class  StudentSemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model= Semester
        fields=["semester"]