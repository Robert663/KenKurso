from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    duration = models.CharField(max_length=10)

    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True)