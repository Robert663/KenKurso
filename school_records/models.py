from django.db import models


class School_Record(models.Model):
    coursing = models.BooleanField(default=True)
    grade = models.IntegerField()
    
    student_id = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    subject_id = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)
