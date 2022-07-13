from django.urls import path
from .views import views

urlpatterns = [
    path('classes/', views.ListClassView.as_view()),
    path('classes/<int:num>', views.ListClassView.as_view()),
    path('classes/subject/<int:subject_id>/', views.ListClassSubjectView.as_view()),
    path('classes/subject/<int:subject_id>/', views.CreateClassSubjectView.as_view()),
    path('classes/<pk>', views.ClassView.as_view()),
]
