from django.db import models

class Teacher(models.Model):
    user_id = models.OneToOneField(("users.User"), on_delete=models.CASCADE)
    contrated_at = models.DateTimeField(datetime.now)

# Create your models here.
