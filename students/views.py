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
from rest_framework.authentication import TokenAuthentication
from .permissions import StudentPermission

class CreateStudent(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[StudentPermission]   

    def post(self, request):
        try:
            course_id = request.data.pop('course')
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response(
                {"message": "Course not found"}, status.HTTP_404_NOT_FOUND
            )
        try:
            semester_id = request.data.pop('semester')
            semester = Semester.objects.get(id=semester_id)
        except Semester.DoesNotExist:
            return Response(
                {"message": "Semester not found"}, status.HTTP_404_NOT_FOUND
            )

        serializer_user = UserSerializers(data=request.data)
        serializer_user.is_valid(raise_exception=True)
        user = serializer_user.save()
        
        student_data = {"semester": semester.id, "course": course.id}
        print(student_data)
        serializer_student = StudentSerializer(data=student_data)

        serializer_student.is_valid(raise_exception=True)
        serializer_student.save(user=user, course=course, semester=semester)
        return Response(serializer_student.data, status=status.HTTP_201_CREATED)

class ListStudents(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RetrieveUpdateStudents(generics.RetrieveUpdateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[StudentPermission]  

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DeactiveStudent(generics.UpdateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[StudentPermission]  
    
    queryset = Student.objects.all()
    serializer_class = DeactiveStudentSerializer



class ListStudentCourseViews(APIView):

    def get(self, request, course_id):

        course = Student.objects.filter(course_id = course_id ).all()
        courseSerializer = StudentSerializer(course, many=True)

        return Response(courseSerializer.data)
    
