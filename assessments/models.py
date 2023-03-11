import os
from pathlib import Path
import random
from django.contrib.staticfiles import finders
import string
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User

from django.db import models

from courses.models import Course


def get_image():
    file_path = finders.find("images/covers")
    files = []
    for f in os.listdir(file_path):
        if os.path.isfile(os.path.join(file_path, f)):
            files.append(f)
    return random.choice(files)


def get_term():
    current_date = datetime.now()
    current_year = current_date.year
    if current_date.month < 8:
        semester = "02"
    else:
        semester = "08"
    return f"{current_year}-{semester}"


def make_valid_file_name(name):
    valid_name = "-_.() %s%s" % (string.ascii_letters, string.digits)
    " ".join([word.capitalize() for word in valid_name.split()])
    cleaned_name = "".join(c if c in valid_name else "-" for c in name)
    return cleaned_name.strip("-")


class Assessment(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cover_image = models.CharField(max_length=100, blank=True)
    upload_folder = models.FilePathField()
    question_paper = models.FileField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_upload_folder(self):
        folder_path = f"{get_term()}/Assessment"
        folder_path = Path(folder_path)
        media_url = settings.MEDIA_ROOT

        counter = 1
        while True:
            full_folder_name = f"{folder_path}-{counter:02d}"
            if not os.path.exists(f"{media_url}/{full_folder_name}"):
                os.makedirs(f"{media_url}/{full_folder_name}")
                break
            counter += 1

        return full_folder_name

    def save(self, *args, **kwargs):
        self.upload_folder = self.get_upload_folder()
        self.question_paper.name = f"{self.upload_folder}/question_paper.pdf"
        self.cover_image = get_image()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
