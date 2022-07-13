from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.CreateStudent.as_view()),
    path('students/', views.ListStudents.as_view()),
    path('students/<pk>/', views.RetrieveUpdateStudents.as_view()),
    path('students/course/<int:course_id>/', views.ListStudentCourseViews.as_view()),
    path('students/<pk>/deactivate/', views.DeactiveStudent.as_view()),
]