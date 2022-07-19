from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, status, Request
from .models import Class
from .serializers import ClassSerializer, UpdateClassSerializer
from subjects.models import Subject
from .mixins import SerializerByMethodMixin


class ListClassView(ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
     
class ListCreateClassSubjectView(APIView):
    def post(self, request: Request, subject_id):
        subject = get_object_or_404(Subject, id=subject_id)
        subjectSerializer = ClassSerializer(data=request.data)
        subjectSerializer.is_valid(raise_exception=True)
        subjectSerializer.save(subject_id=subject.id)
        return Response(subjectSerializer.data, status.HTTP_201_CREATED)

    def get(self, request, subject_id):
        subject = Class.objects.filter(subject_id = subject_id).all()
        if len(subject)==0:
            return Response({"message":"Subject not attributed to any class"}, status.HTTP_404_NOT_FOUND)
        subjectSerializer = ClassSerializer(subject, many=True)
        return Response(subjectSerializer.data)


class ClassView(SerializerByMethodMixin, RetrieveUpdateDestroyAPIView):

    queryset = Class.objects.all()
    serializer_map ={
        'GET':ClassSerializer,
        'PATCH':UpdateClassSerializer,
    } 
