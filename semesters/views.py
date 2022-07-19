from rest_framework import generics
from rest_framework.views import APIView, Response, status
from courses.models import Course
from rest_framework.authentication import TokenAuthentication
from .permissions import SuperUserPermission
from semesters.models import Semester
from semesters.serializers import SemesterSerializers

class SemestersCourseView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[SuperUserPermission]    
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
            semester = Semester.objects.filter(course_id=course_id).all()
            serializer = SemesterSerializers(semester, many=True)
            return Response(serializer.data)

class SemesterView(generics.RetrieveAPIView):
    queryset=Semester.objects.all()
    serializer_class=SemesterSerializers
  