from rest_framework import generics
from teachers.models import Teacher
from teachers.serializers import TeacherSerializers


class ListTeacher(generics.ListAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()


class DetailsTeacher(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()
