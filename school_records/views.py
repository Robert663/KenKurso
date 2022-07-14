from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, status, Request
from .models import School_Record
from .serializers import SchoolRecordSerializers
from students.models import Student

class ListRecord(ListAPIView):

    serializer_class = SchoolRecordSerializers
    queryset = School_Record.objects.all()


class DetailsRecord(RetrieveUpdateDestroyAPIView):

    serializer_class = SchoolRecordSerializers
    queryset = School_Record.objects.all()


class CreateRecordStudent(APIView):

    def post(self, request: Request, student_id):

        student = get_object_or_404(Student, pk=student_id)
        schoolRecordSerializer = SchoolRecordSerializers(data=request.data)
        schoolRecordSerializer.is_valid(raise_exception=True)
        schoolRecordSerializer.save(student_id=student)

        return Response(schoolRecordSerializer.data, status.HTTP_201_CREATED)


class ListRecordStudent(ListAPIView):

    def get(self, request, student_id):

        student = School_Record.objects.filter(student_id = student_id ).all()
        studentSerializer = SchoolRecordSerializers(student)

        return Response(studentSerializer.data)


class ListRecordSubject(APIView):

    def get(self, request, subject_id):

        subject = School_Record.objects.filter(subject_id = subject_id ).all()
        subjectSerializer = SchoolRecordSerializers(subject)

        return Response(subjectSerializer.data)