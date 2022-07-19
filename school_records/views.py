from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, status, Request
from .models import School_Record
from .permissions import SuperUserPermission, StudentPermission
from .serializers import SchoolRecordSerializers
from rest_framework.authentication import TokenAuthentication
from students.models import Student

class ListRecord(ListAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[SuperUserPermission]  
    serializer_class = SchoolRecordSerializers
    queryset = School_Record.objects.all()


class DetailsRecord(RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[StudentPermission]  
    serializer_class = SchoolRecordSerializers
    queryset = School_Record.objects.all()


class CreateRecordStudent(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[StudentPermission]  
    def post(self, request: Request, student_id):

        student = get_object_or_404(Student, pk=student_id)
        schoolRecordSerializer = SchoolRecordSerializers(data=request.data)
        schoolRecordSerializer.is_valid(raise_exception=True)
        schoolRecordSerializer.save(student_id=student.user.id)

        return Response(schoolRecordSerializer.data, status.HTTP_201_CREATED)


class ListRecordStudent(ListAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[StudentPermission]  
    def get(self, request, student_id):

        student = School_Record.objects.filter(student_id = student_id ).all()
        studentSerializer = SchoolRecordSerializers(student, many=True)

        return Response(studentSerializer.data)


class ListRecordSubject(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[SuperUserPermission] 
    def get(self, request, subject_id):

        subject = School_Record.objects.filter(subject_id = subject_id ).all()
        subjectSerializer = SchoolRecordSerializers(subject, many=True)

        return Response(subjectSerializer.data)