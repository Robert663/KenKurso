from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, status
from school_records.models import School_Record
from school_records.serializers import SchoolRecordSerializers
from semesters.serializers import SemesterSerializers
from teachers.models import Teacher
from .models import Subject
from .serializers import SubjectSerializers
from semesters.models import Semester
from courses.models import Course
from rest_framework.authentication import TokenAuthentication
from .permissions import subjectPermission

class ListSubjectsView(ListAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers

class ListSubjectCourseView(APIView):

    def get(self, request, course_id):
        try:
            Course.objects.get(id=course_id)
        except:
            return Response({"message":"Course not found"}, status.HTTP_404_NOT_FOUND)
        semesters = Semester.objects.filter(course_id = course_id).all()
        subjectsSerializer = SemesterSerializers(semesters, many=True)
        return Response(subjectsSerializer.data)


class ListSubjectTeacherView(APIView):

    def get(self, request, teacher_id):
        try:
             Teacher.objects.get(user=teacher_id)
        except:
            return Response({"message":"Teacher not found"},status.HTTP_404_NOT_FOUND)

        teacher_subjects = Subject.objects.filter(teacher_id = teacher_id).all()
        teacher_serializer = SubjectSerializers(teacher_subjects, many=True)

        return Response(teacher_serializer.data)


class CreateSubjectView(CreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[subjectPermission]

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers


class SubjectView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[subjectPermission]

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers