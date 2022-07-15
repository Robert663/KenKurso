from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, status

from school_records.models import School_Record
from school_records.serializers import SchoolRecordSerializers
from semesters.serializers import SemesterSerializers
from .models import Subject
from .serializers import SubjectSerializers
from semesters.models import Semester
from courses.models import Course

# class ListSubjectView(ListAPIView):

#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializers

#     def get_queryset(self):
#         amount_subject = self.kwargs["num"]
#         return self.queryset.order_by("-date_joined")[0:amount_subject]

class ListSubjectsView(ListAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers


class ListSubjectCourseView(APIView):

    def get(self, request, course_id):
        # subject_data = []
        try:
            Course.objects.get(id=course_id)
        except:
            return Response({"message":"Course not found"}, status.HTTP_404_NOT_FOUND)
        semesters = Semester.objects.filter(course_id = course_id).all()
        # print("TEST SUBJECT",semesters[1])
        # for item in semesters:
        #     for subject in item.subjects_id:
        #         subject_data.append(subject)
        subjectsSerializer = SemesterSerializers(semesters, many=True)
        return Response(subjectsSerializer.data)


class ListSubjectTeacherView(APIView):

    def get(self, request, teacher_id):

        teacher = School_Record.objects.filter(teacher_id = teacher_id).all()
        teacherSerializer = SchoolRecordSerializers(teacher, many=True)

        return Response(teacherSerializer.data)


class CreateSubjectView(CreateAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers


class SubjectView(RetrieveUpdateDestroyAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers