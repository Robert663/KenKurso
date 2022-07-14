from django.urls import path
from . import views

urlpatterns = [
    path('semester/course/<int:course_id>/', views.SemestersCourseView.as_view()),
    path('semester/<int:semester_id>/', views.SemesterView.as_view()),
]