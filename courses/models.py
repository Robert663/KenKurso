from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=127, null=False)
    description = models.TextField(null=False)
    duration = models.IntegerField(null=False)
    inscriptions = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
