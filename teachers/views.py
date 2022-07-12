from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from courses.models import Course
from semesters.models import Semester
from students.serializers import StudentSerializer
from teachers.serializers import TeacherSerializers
from users.serializers import UserSerializers


class CreateTeacher(APIView):
    def post(self, request):
        serializer_user = UserSerializers(data=request.data)
        serializer_user.is_valid(raise_exception=True)
        user = serializer_user.save(is_staff=True)

        serializer_teacher = TeacherSerializers(data=user)
        serializer_teacher.is_valid(raise_exception=True)
        serializer_teacher.save()
        return Response(serializer_teacher.data, status=status.HTTP_201_CREATED)
