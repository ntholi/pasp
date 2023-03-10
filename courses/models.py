from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    lecturers = models.ManyToManyField(User)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     user = kwargs.pop('user', None)
    #     self.lecturers.add(user)
    #     super().save(*args, **kwargs)