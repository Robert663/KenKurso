from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from courses.models import Course
from semesters.models import Semester
from students.serializers import StudentSerializer
from users.serializers import UserSerializers
from rest_framework import generics
from students.models import Student
from students.serializers import DeactiveStudentSerializer, StudentSerializer
from django.shortcuts import get_object_or_404


class CreateStudent(APIView):
    def post(self, request):
        course_id = request.data.pop('course')
        course = get_object_or_404(Course, id=course_id)

        semester_id = request.data.pop('semester')
        semester = get_object_or_404(Semester, id=semester_id)

        serializer_user = UserSerializers(data=request.data)
        serializer_user.is_valid(raise_exception=True)
        user = serializer_user.save()
        print("VEJA SEU CEGO 0><<",type(user))

        student_data = {"user_id":user.id, "semester": semester.id, "course": course.id}
        print("VEJA SEU CEGO 1><<",student_data)

        serializer_student = StudentSerializer(data=student_data)
        print("VEJA SEU CEGo 2><<",student_data)

        serializer_student.is_valid(raise_exception=True)
        print("VEJA SEU CEGO 3><<",student_data)

        serializer_student.save()
        return Response(serializer_student.data, status.HTTP_201_CREATED)

class ListStudents(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RetrieveUpdateStudents(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DeactiveStudent(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = DeactiveStudentSerializer



class ListStudentCourseViews(APIView):

    def get(self, request, course_id):

        course = Student.objects.filter(course_id = course_id ).all()
        courseSerializer = StudentSerializer(course, many=True)

        return Response(courseSerializer.data)
    
