from django.db import models

class School_Record(models.Model):
    coursing = models.BooleanField(default=True)
    grade = models.IntegerField()
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)
