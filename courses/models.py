from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    lecturers = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

    def lecturer_names(self):
        return ", ".join([user.get_full_name() for user in self.lecturers.all()])
