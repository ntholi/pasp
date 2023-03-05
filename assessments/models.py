import os
from pathlib import Path
import random
import uuid
from django.contrib.staticfiles import finders
import string
from datetime import datetime
from django.conf import settings

from django.db import models


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
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    lecturer = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    course_name = models.CharField(max_length=100)
    question_paper = models.FileField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cover_image = models.CharField(max_length=100, blank=True)
    upload_folder = models.FilePathField()
    date_created = models.DateTimeField(auto_now_add=True)

    def get_upload_folder(self):
        lecturer = make_valid_file_name(self.lecturer)
        folder_path = f"{get_term()}/{lecturer}/Assessment"
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
        return self.title
