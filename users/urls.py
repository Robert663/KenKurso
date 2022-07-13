from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CreateStudent.as_view()),
    path('users/<int: num>/', views.UserView.as_view()),
    path('users/<pk>/', views.UpdateUserView.as_view()),
    path('users/coordination/', views.SuperUserView.as_view()),
    path('users/login/', views.LoginUserView.as_view()),
]