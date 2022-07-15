from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, status, Request
from .models import Course
from .serializers import CourseSerializer
from students.models import Student
from students.serializers import StudentDisplaySerializer

class ListCreateCourseView(ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class DetailsCourseView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class ListStudentCourse(ListAPIView):
    def get(self, request, course_id):

        student = Student.objects.filter(course_id=course_id).all()
        course = Course.objects.get(id=course_id)
        course_serializer = CourseSerializer(course)
        student_serializer = StudentDisplaySerializer(student, many=True)
        response_data = {"course":course_serializer.data, "students":student_serializer.data}

        return Response(response_data)
