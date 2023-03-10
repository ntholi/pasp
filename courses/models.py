from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    lecturers = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name} ({self.code})"
