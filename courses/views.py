from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, status, Request
from .models import Course
from .serializers import CourseSerializer
from students.models import Student
from students.serializers import StudentSerializer

class ListCreateCourseView(ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class DetailsCourseView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class ListStudentCourse(ListAPIView):
    def get(self, request, student_id):

        student = Student.objects.filter(course_id=student_id).all()

        student_serializer = StudentSerializer(student, many=True)

        return Response(student_serializer.data)
