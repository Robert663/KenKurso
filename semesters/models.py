from django.db import models


class Semester(models.Model):
    semester = models.IntegerField()
    course_id = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    subjects_id = models.ManyToManyField('subjects.Subject', related_name='semester')
