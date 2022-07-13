from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/', views.SemestersCourseView.as_view()),
    path('<int:semester_id>/', views.SemesterView.as_view()),
]