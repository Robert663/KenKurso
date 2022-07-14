from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.CreateTeacher.as_view()),
    path('teacher/', views.ListTeacher.as_view()),
    path('teacher/<pk>/', views.DetailsTeacher.as_view()),
] 