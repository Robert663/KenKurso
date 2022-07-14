from rest_framework import serializers
from .models import Semester


class SemesterSerializers(serializers.ModelSerializer):

    class Meta:
        model = Semester
        fields = ["semester", "course_id", "subjects_id"]
