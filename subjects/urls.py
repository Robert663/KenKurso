from django.urls import path
from . import views


urlpatterns = [

    path('subjects/', views.ListSubjectsView.as_view()),
    path('subjects/<pk>/', views.SubjectView.as_view()),
    path('subjects/teacher/<int:teacher_id>/', views.ListSubjectTeacherView.as_view()),
    path('subjects/course/<int:course_id>/', views.ListSubjectCourseView.as_view()),
    path('subject/', views.CreateSubjectView.as_view()),
    path('subjects/<pk>/', views.SubjectView.as_view()),
]
