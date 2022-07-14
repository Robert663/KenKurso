from urllib import response
from rest_framework import generics
from rest_framework.views import APIView, Response, status
from yaml import serialize
from courses.models import Course

from semesters.models import Semester
from semesters.serializers import SemesterSerializers

class SemestersCourseView(APIView):
    def post(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except:
            return Response({"message":"Course not found"}, status.HTTP_404_NOT_FOUND)    
        serializer = SemesterSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(course_id=course.id)
        return Response(serializer.data, status.HTTP_201_CREATED)
    def get(self, request, course_id):
        try:
            semester = Semester.objects.get(course_id=course_id)
            serializer = SemesterSerializers(semester)
            return Response(serializer.data)
        except:
            return Response({"message":"Course not found"}, status.HTTP_404_NOT_FOUND)

class SemesterView(generics.ListCreateAPIView):
    queryset=Semester.objects.all()
    serializer_class=SemesterSerializers
    def get_queryset(self):
        semester = self.kwargs["semester_id"]
        return self.queryset.filter(id=semester)