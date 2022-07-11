from django.db import models


class Student(models.Model):
    active = models.BooleanField(default=True)

    user_id = models.OneToOneField('users.User', on_delete=models.CASCADE, primary_key=True)
    course_id = models.OneToOneField('courses.Course', on_delete=models.CASCADE, primary_key=True)
