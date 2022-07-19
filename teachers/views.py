
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from courses.models import Course
from semesters.models import Semester
from students.serializers import StudentSerializer
from teachers.serializers import TeacherSerializers
from users.serializers import UserSerializers
from rest_framework import generics
from teachers.models import Teacher
from teachers.serializers import TeacherSerializers
from rest_framework.authentication import TokenAuthentication
from .permissions import teacherPermission

class CreateTeacher(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[teacherPermission]   

    def post(self, request):
        serializer_user = UserSerializers(data=request.data)
        serializer_user.is_valid(raise_exception=True)
        user = serializer_user.save(is_staff=True)
        data_user={"user": user.id}
        serializer_teacher = TeacherSerializers(data=data_user)
        serializer_teacher.is_valid(raise_exception=True)
        serializer_teacher.save()
        return Response(serializer_teacher.data, status=status.HTTP_201_CREATED)
        
class ListTeacher(generics.ListAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()

class DetailsTeacher(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[teacherPermission]   

    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()

