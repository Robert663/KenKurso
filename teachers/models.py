from django.db import models


class Teacher(models.Model):
    user = models.OneToOneField(("users.User"), on_delete=models.CASCADE, primary_key=True)
    contracted_at =  models.DateTimeField(auto_now_add=True)

