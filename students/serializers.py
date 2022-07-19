from rest_framework.serializers import ModelSerializer
from courses.serializers import CourseSerializer
from semesters.serializers import StudentSemesterSerializer
from users.serializers import UserSerializers
from .models import Student


class StudentDisplaySerializer(ModelSerializer):
    user = UserSerializers(read_only=True)

    class Meta:
        model = Student
        fields = ["active", "user", "semester"]
        depth = 0


class StudentSerializer(ModelSerializer):
    user = UserSerializers(read_only=True)
    course = CourseSerializer(read_only=True)
    semester = StudentSemesterSerializer(read_only=True)

    class Meta:
        model = Student
        fields = "__all__"


    def create(self, validated_data):
        print(validated_data)
        return Student.objects.create(**validated_data)


class UpdateStudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class DeactiveStudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ["active"]

    def update(self, instance, validated_data):
        validated_data["active"] = False
        return super().update(instance, validated_data)
