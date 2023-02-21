import os
import random
import uuid
from django.contrib.staticfiles import finders
from django.core.validators import FileExtensionValidator

from django.db import models


def get_image():
    file_path = finders.find("images/covers")
    files = []
    for f in os.listdir(file_path):
        if os.path.isfile(os.path.join(file_path, f)):
            files.append(f)
    return random.choice(files)


class Assessment(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    lecturer = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, blank=True)
    question_paper = models.FileField(upload_to="question_papers/", blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cover_image = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        # self.question_paper.name = (
        #     f"{self.uuid}.pdf"
        # )
        self.cover_image = get_image()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
