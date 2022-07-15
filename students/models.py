from django.db import models


class Student(models.Model):
    active = models.BooleanField(default=True)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, primary_key=True)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='students')
    semester = models.OneToOneField('semesters.Semester', on_delete=models.CASCADE)
