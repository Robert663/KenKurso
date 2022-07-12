from rest_framework import generics

from students.models import Student
from students.serializers import DeactiveStudentSerializer, StudentSerializer


class ListStudents(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RetrieveUpdateStudents(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DeactiveStudent(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = DeactiveStudentSerializer
    
    