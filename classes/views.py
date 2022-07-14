from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, status, Request
from .models import Class
from .serializers import ClassSerializer
from subjects.models import Subject


class ListClassView(ListAPIView):

    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def get_queryset(self):
        amount_class = self.kwargs["num"]
        return self.queryset.order_by("-date_joined")[0:amount_class]


class ListClassSubjectView(APIView):

    def get(self, request, subject_id):

        subject = Class.objects.filter(subject_id = subject_id).all()
        subjectSerializer = ClassSerializer(subject)

        return Response(subjectSerializer.data)


class CreateClassSubjectView(APIView):

    def post(self, request: Request, subject_id):

        subject = get_object_or_404(Subject, pk=subject_id)
        subjectSerializer = ClassSerializer(data=request.data)
        subjectSerializer.is_valid(raise_exception=True)
        subjectSerializer.save(subject_id=subject)

        return Response(subjectSerializer.data, status.HTTP_201_CREATED)


class ClassView(RetrieveUpdateDestroyAPIView):

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
