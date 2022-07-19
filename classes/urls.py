from django.urls import path
from . import views

urlpatterns = [
    path('classes/', views.ListClassView.as_view()),
    path('classes/subjects/<int:subject_id>/', views.ListCreateClassSubjectView.as_view()),
    path('classes/<pk>/', views.ClassView.as_view()),
]
