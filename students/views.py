from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from courses.models import Course
from semesters.models import Semester
from students.serializers import StudentSerializer
from users.serializers import UserSerializers


class CreateStudent(APIView):
    def post(self, request):
        course_id = request.data.pop('course')
        course = Course.objects.get(id=course_id)

        semester_id = request.data.pop('semester')
        semester = Semester.objects.get(id=semester_id)

        serializer_user = UserSerializers(data=request.data)
        serializer_user.is_valid(raise_exception=True)
        user = serializer_user.save()

        student_data = {user, semester, course}
        serializer_student = StudentSerializer(data=student_data)
        serializer_student.is_valid(raise_exception=True)
        serializer_student.save()
        return Response(serializer_student.data, status=status.HTTP_201_CREATED)
