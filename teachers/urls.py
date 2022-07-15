from django.urls import path
from . import views

urlpatterns = [
    path('teacher/<pk>/', views.DetailsTeacher.as_view()),
    path('teacher/', views.CreateTeacher.as_view()),
    path('teachers/', views.ListTeacher.as_view()),
] 