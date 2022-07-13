from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, status
from .models import Subject
from .serializers import SubjectSerializers


class ListSubjectView(ListAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers

    def get_queryset(self):
        amount_subject = self.kwargs["num"]
        return self.queryset.order_by("-date_joined")[0:amount_subject]



class ListSubjectCourseView(APIView):

    def get(self, request, course_id):

        course = School_Record.objects.filter(course_id = course_id).all()
        courseSerializer = SchoolRecordSerializers(course)

        return Response(courseSerializer.data)


class ListSubjectTeacherView(APIView):

    def get(self, request, teacher_id):

        teacher = School_Record.objects.filter(teacher_id = teacher_id).all()
        teacherSerializer = SchoolRecordSerializers(teacher)

        return Response(teacherSerializer.data)


class CreateSubjectView(CreateAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers


class SubjectView(RetrieveUpdateDestroyAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers