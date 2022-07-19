
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from teachers.serializers import TeacherSerializers
from users.serializers import UserSerializers
from rest_framework import generics
from teachers.models import Teacher
from teachers.serializers import TeacherSerializers


class CreateTeacher(APIView):
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
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()

