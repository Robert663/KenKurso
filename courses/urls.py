from django.urls import path
from .views import views

urlpatterns = [
    path("courses/", views.ListCourseView.as_view()),
    path("courses/<pk>/", views.DetailsCourseView.as_view()),
    path("courses/students/<int: student_id>/", views.ListStudentCourse.as_view())
]