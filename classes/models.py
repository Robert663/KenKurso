from django.db import models


class Class(models.Model):
    title = models.CharField(max_length=70)
    text = models.TextField()
    video = models.CharField(max_length=300)
    graded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField()


    subject = models.OneToOneField('subjects.Subject', on_delete=models.CASCADE)
