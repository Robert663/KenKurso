from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.views import APIView, Response, status, Request
from .models import Course
from .serializers import CourseSerializer
from students.models import Student


class ListCreateCourseView(ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class DetailsCourseView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class ListStudentCourse(ListAPIView):
    def get(self, request, student_id):

        student = Course.objects.filter(student_id=student_id).all()
        studentSerializer = CourseSerializer(student)

        return Response(studentSerializer.data)
