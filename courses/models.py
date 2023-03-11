from django.contrib.auth.models import User
from django.db import models

__colors = (
    '#6A1B9A',
    '#4527A0',
    '#283593',
    '#1565C0',
    '#0277BD',
    '#00838F',
    '#00695C',
    '#2E7D32',
    '#424242',
    '#37474F',
)


def get_random_color():
    import random
    return random.choice(__colors)


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    lecturers = models.ManyToManyField(User)
    color = models.CharField(max_length=7, default=get_random_color)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

    def lecturer_names(self):
        return ", ".join([user.get_full_name() for user in self.lecturers.all()])
