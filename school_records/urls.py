from django.urls import path
from . import views

urlpatterns = [
    path("records/", views.ListRecord.as_view()),
    path("records/students/<int:student_id>/", views.ListRecordStudent.as_view()),
    path("records/student/<int:student_id>/", views.CreateRecordStudent.as_view()),
    path("records/subject/<int:subject_id>/", views.ListRecordSubject.as_view()),
    path("records/<pk>/", views.DetailsRecord.as_view())
]   