from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.ListCreateCourseView.as_view()),
    path("courses/<pk>/", views.DetailsCourseView.as_view()),
    path("courses/students/<int:course_id>/", views.ListStudentCourse.as_view())
]